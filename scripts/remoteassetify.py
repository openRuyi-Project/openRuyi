#!/usr/bin/env python3

# Required utilities:
# - util-linux: enosys (optional with --unsafe-optional-enosys)
# - rpm: rpmspec
# - curl

from typing import *

import argparse
import hashlib
import pathlib
import re
import shlex
import shutil
import subprocess
import sys

arg_parser = argparse.ArgumentParser(
    prog=sys.argv[0],
    description='Generate a patch to update #!RemoteAsset lines',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog = f'''{sys.argv[0]} does not edit spec files directly.
Pipe the output into 'git apply' to apply the patch:

$ {sys.argv[0]} SPECS/<package>/<package>.spec | git apply
''',
)

arg_parser.add_argument('filename', metavar='SPECS/pkg/pkg.spec', nargs='?', help='Path to spec file to process')
arg_parser.add_argument('--dry-run', action='store_true', help='Print found remote assets only, do not download')
arg_parser.add_argument('--verbose', action='store_true', help='Generate more debug output')
arg_parser.add_argument('--unsafe-optional-enosys', action='store_true', help='UNSAFE: Allow running rpmspec without enosys')
arg_parser.add_argument('--workflow', action='store_true', help='Generate some messages as workflow commands')

# Initialized in main()
args: argparse.Namespace

CURL_DOWNLOAD = shlex.split("""curl --fail --location --proto '=http,https' --user-agent 'scripts/remoteassetify.py openruyi.cn' -o""")

CHECKSUM_TYPES = { 'sha256' }

def message(prefix: str, text: str, line_num: Optional[int] = None, line_text: Optional[str] = None):
    PREFIX_MAP = { 'WARN': 'warning', 'INFO': 'notice' }

    if line_num is not None:
        append_msg = f" in line {line_num + 1}:\n    > {line_text if line_text else '(empty)'}"
        additional_tags = f',line={line_num + 1}'
    else:
        append_msg = ''
        additional_tags = ''

    print(f'{prefix}: {text}{append_msg}', file=sys.stderr)

    if args.workflow:
        workflow_prefix = PREFIX_MAP.get(prefix, 'notice')
        print(f'::{workflow_prefix} file={args.filename}{additional_tags}::{text}', file=sys.stderr)

def spec_filter(text: str) -> str:
    GOOD = [
        r'^Source\d*:',
        r'^(Name|Version|Release|Summary|License|URL|VCS|Description):',
        r'^%(description|package|global|define|if\w*|else|endif)(\s+|$)',
    ]

    BAD = [
        r'%\(',             # Runs a shell command
        r'%{lua:',          # Runs Lua code
        r'^%.+\{[^}]*$',    # Definitely an incomplete macro
        r'\\$',             # Line continuation, incomplete
    ]

    result = []
    for line in text.splitlines():
        if not any(re.search(r, line, re.IGNORECASE) for r in GOOD):
            continue

        if line.startswith('%if'):
            line = '%if 1'

        if any(re.search(r, line, re.IGNORECASE) for r in BAD):
            continue

        result.append(line)

    return ''.join(l + '\n' for l in result)

def rpmspec_parse_command() -> list[str]:
    if shutil.which('enosys') is not None:
        # Block executing other programs
        return shlex.split("""enosys -s execve -s execveat -- rpmspec -D '%autorelease 0' -D '%_lto_cflags %nil' --parse /dev/stdin""")
    else:
        if not args.unsafe_optional_enosys:
            raise RuntimeError('Unable to find enosys. To allow running rpmspec without enosys, use --unsafe-optional-enosys')

        print('WARN: enosys not found, running rpmspec without blocking command execution', file=sys.stderr)
        return shlex.split("""rpmspec -D '%autorelease 0' -D '%_lto_cflags %nil' --parse /dev/stdin""")

def rpmspec_parse(text: str) -> str:
    proc = subprocess.run(rpmspec_parse_command(), capture_output=True, input=text.encode())
    msg = proc.stderr.decode('utf-8', errors='replace').strip()

    try:
        proc.check_returncode()
    except subprocess.CalledProcessError as e:
        e.add_note(f"NOTE: Filtered spec: \n{text if text else '(EMPTY)'}\n")
        e.add_note(f"NOTE: rpmspec says: \n{msg if msg else '(EMPTY)'}\n")
        raise e

    if args.verbose:
        print(f"NOTE: Filtered spec: \n{text if text else '(EMPTY)'}\n", file=sys.stderr)

        if msg:
            print(f'NOTE: rpmspec says (probably benign):\n{msg}\n', file=sys.stderr)

    return proc.stdout.decode('utf-8', errors='replace')

def get_name(text: str) -> str:
    for line in text.splitlines():
        if ':' not in line:
            continue

        key, value = line.split(':', 1)
        if key.lower() == 'name':
            return value.strip()

    raise ValueError('No Name found in spec')

class RemoteAssetData(NamedTuple):
    lineno: int
    checksum_type: str | None
    checksum: str | None

def get_sources(text: str) -> dict[str, str]:
    result = {}

    for line in text.splitlines():
        if ':' not in line:
            continue

        key, value = line.split(':', 1)
        m = re.match(r'^Source\d*$', key, re.IGNORECASE)
        if not m:
            continue

        result[key] = value.strip()

    return result

def get_remoteasset_lines(text: str) -> dict[str, RemoteAssetData]:
    lines = text.splitlines()

    result = {}
    for i, line in enumerate(lines):
        line = line.strip()

        if line == '#!RemoteAsset':
            checksum_type = None
            checksum = None
        elif line.startswith('#!RemoteAsset:'):
            parts = line.split(maxsplit=2)
            if len(parts) == 1:
                # e.g. #!RemoteAsset:
                checksum_type = None
                checksum = None
            elif len(parts) == 2 and re.match(r'^\w+:\w+$', parts[1]):
                # e.g. #!RemoteAsset: sha256:0000
                checksum_type = parts[1].split(':', 1)[0]
                checksum = parts[1].split(':', 1)[1]
            else:
                message('INFO', 'Unhandled #!RemoteAsset format ignored', i, line)
                continue

        else:
            continue

        if i == len(lines) - 1:
            message('WARN', 'Unexpected #!RemoteAsset line at end of file', i, line)
            continue

        next_line = lines[i + 1].strip()
        if ':' not in next_line:
            message('WARN', 'Unexpected Source line format', i + 1, next_line)
            continue

        key, value = next_line.split(':', 1)
        m = re.match(r'^Source\d*$', key, re.IGNORECASE)

        if not m:
            message('WARN', f'Unhandled remote asset with key {key}', i + 1, next_line)
            continue

        result[key] = RemoteAssetData(
            lineno=i,
            checksum_type=checksum_type,
            checksum=checksum
        )

    return result

def download_asset(outdir: pathlib.Path, url: str) -> pathlib.Path | None:
    outdir.mkdir(parents=True, exist_ok=True)
    orig_base = url.rsplit('/', 1)[-1]
    base = re.sub(r'[^\w.-]', '_', orig_base)
    if base != orig_base:
        print(f'WARN: Sanitized file name to {base}')

    out_path = outdir / base

    # I know urllib exists, but having a copiable curl command is nicer
    command = [*CURL_DOWNLOAD, str(out_path), '--', url]

    print(f'$ {shlex.join(command)}', file=sys.stderr)
    proc = subprocess.run(command)

    if proc.returncode == 0:
        return out_path
    else:
        return None

def main():
    global args

    args = arg_parser.parse_args()

    if args.filename is None:
        args.filename = 'STDIN'

        if sys.stdin.isatty():
            print('WARN: Reading spec file from stdin...', file=sys.stderr)
        spec = sys.stdin.read()
    else:
        if args.filename[0] == '/':
            print('WARN: Absolute path specified, patch will probably not work', file=sys.stderr)

        with open(args.filename) as f:
            spec = f.read()

    spec_noeol = spec and spec[-1] != '\n'

    parsed = rpmspec_parse(spec_filter(spec))
    pkg_name = get_name(parsed)

    print(f'INFO: Processing package: {pkg_name}', file=sys.stderr)

    sources = get_sources(parsed)
    assets = get_remoteasset_lines(spec)

    spec_lines = spec.splitlines()

    if not assets:
        print('INFO: No supported #!RemoteAsset found', file=sys.stderr)
        return

    for key, data in assets.items():
        if key not in sources:
            raise ValueError(f'{key} key not found in parsed spec, that is odd')

        url = sources[key]

        if ':' not in url:
            message('WARN', f'Unrecognized URL: {url}', data.lineno + 1, spec_lines[data.lineno + 1])
        elif re.search(r'%[a-z_{]', url, re.IGNORECASE):
            message('WARN', f'Possible unexpanded RPM macro in URL: {url}', data.lineno + 1, spec_lines[data.lineno + 1])

    if args.dry_run:
        if sys.stdout.isatty():
            print('INFO: Found remote assets:', file=sys.stderr)
            print(file=sys.stderr)

        for key, data in assets.items():
            if data.checksum_type:
                checksum_type, checksum = data.checksum_type, data.checksum
                print(f'{key}: {sources[key]} {checksum_type}:{checksum}')
            else:
                print(f'{key}: {sources[key]}')

        return
    else:
        print('INFO: Found remote assets:', file=sys.stderr)

        for key, data in assets.items():
            lineno = data.lineno

            if data.checksum_type:
                checksum_type, checksum = data.checksum_type, data.checksum
                print(f'{lineno + 1:4}: {key}: {sources[key]} {checksum_type}:{checksum}', file=sys.stderr)
            else:
                print(f'{lineno + 1:4}: {key}: {sources[key]} (Unknown checksum)', file=sys.stderr)

    outdir = pathlib.Path('_assets') / pkg_name

    any_changed = False
    failed = []
    differ = []
    patch_lines = []

    for key, data in assets.items():
        if data.checksum_type not in CHECKSUM_TYPES:
            checksum_type = 'sha256'
            if data.checksum_type is not None:
                print(f"WARN: Unknown checksum type {data.checksum_type}, using {checksum_type}", file=sys.stderr)
        else:
            checksum_type = data.checksum_type
            old_checksum = data.checksum

        print(f'INFO: Downloading {key}', file=sys.stderr)
        out_path = download_asset(outdir, sources[key])

        if out_path is None:
            message('WARN', f'Failed to download {key} from {sources[key]}', data.lineno + 1, spec_lines[data.lineno + 1])
            failed.append(key)
            continue

        with out_path.open('rb') as out_file:
            new_checksum = hashlib.file_digest(out_file, checksum_type).hexdigest()
            print(f'$ cksum --untagged -a {shlex.join([checksum_type, str(out_path)])}', file=sys.stderr)
            print(f'{new_checksum}  {out_path}', file=sys.stderr)

        if checksum_type != data.checksum_type or new_checksum != old_checksum:
            any_changed = True

            if checksum_type == data.checksum_type:
                differ.append(key)
                print(f'WARN: Checksum changed for {key}, was {checksum_type}:{old_checksum}, now {checksum_type}:{new_checksum}', file=sys.stderr)

            new_remoteasset_line = f'#!RemoteAsset:  {checksum_type}:{new_checksum}'

            print(f'INFO: New #!RemoteAsset line for {key}:', file=sys.stderr)
            print(f'    > {new_remoteasset_line}', file=sys.stderr)

            if args.workflow:
                print(f"::warning file={args.filename},line={data.lineno + 1}::{new_remoteasset_line}", file=sys.stderr)

            patch_lines.append(f'--- a/{args.filename}')
            patch_lines.append(f'+++ b/{args.filename}')
            patch_lines.append(f"@@ -{data.lineno + 1},2 +{data.lineno + 1},2 @@")
            patch_lines.append(f"-{spec_lines[data.lineno]}")
            patch_lines.append(f'+{new_remoteasset_line}')
            patch_lines.append(f" {spec_lines[data.lineno + 1]}")
            if data.lineno == len(spec_lines) - 2 and spec_noeol:
                patch_lines.append('\\ No newline at end of file')
            patch_lines.append('')

    exit_code = 0

    if any_changed:
        if sys.stdout.isatty():
            print(f'INFO: Patch for {args.filename}:', file=sys.stderr)
            print(file=sys.stderr)

        print('\n'.join(patch_lines))

        if differ:
            print(f"WARN: Checksums differ for: {', '.join(differ)}", file=sys.stderr)
        print(f'WARN: #!RemoteAsset lines for {args.filename} requires updating', file=sys.stderr)

        exit_code = 1
    else:
        print(f'INFO: #!RemoteAsset lines for {args.filename} are up to date', file=sys.stderr)

    if failed:
        print(f"WARN: Downloads have failed for: {', '.join(failed)}", file=sys.stderr)
        exit_code = 1

    if exit_code != 0:
        sys.exit(exit_code)

if __name__ == '__main__':
    main()
