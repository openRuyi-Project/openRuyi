# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Exercise the installed Python binding and guestmount with a temporary image."""

import contextlib
import errno
import os
from pathlib import Path
import selectors
import subprocess
import tempfile
import sys
import time


@contextlib.contextmanager
def handle(image, readonly=False):
    import guestfs

    g = guestfs.GuestFS(python_return_dict=True)
    try:
        g.add_drive_opts(str(image), format="raw", readonly=readonly)
        g.launch()
        yield g
        g.shutdown()
    finally:
        g.close()


@contextlib.contextmanager
def host_mount(image, directory, readonly=False):
    read_fd, write_fd = os.pipe()
    command = ["guestmount", "--no-fork", "--fd", str(write_fd),
               "--format=raw", "-a", str(image), "-m", "/dev/sda1"]
    if readonly:
        command.append("--ro")
    command.append(str(directory))
    process = None
    mounted = False
    try:
        process = subprocess.Popen(command, pass_fds=(write_fd,))
        os.close(write_fd)
        write_fd = None
        with selectors.DefaultSelector() as selector:
            selector.register(read_fd, selectors.EVENT_READ)
            if not selector.select(timeout=600) or not os.read(read_fd, 1):
                raise RuntimeError("guestmount did not signal a successful mount")
        mounted = True
        yield
    finally:
        os.close(read_fd)
        if write_fd is not None:
            os.close(write_fd)
        try:
            if mounted:
                subprocess.run(["guestunmount", str(directory)], check=True,
                               timeout=60)
            if process is not None:
                status = process.wait(timeout=60)
                if mounted and status != 0:
                    raise RuntimeError(f"guestmount exited with status {status}")
        finally:
            if process is not None and process.poll() is None:
                process.kill()
                process.wait()


def probe_host(binary):
    """Check host permissions with the independent, existing FUSE 3 stack."""
    if not os.access("/dev/fuse", os.R_OK | os.W_OK):
        print("SKIP: FUSE 3 host probe: /dev/fuse is unavailable", flush=True)
        return 77
    with tempfile.TemporaryDirectory(prefix="fuse3-host-probe-") as temporary:
        directory = Path(temporary)
        mountpoint = directory / "mount"
        mountpoint.mkdir()
        mounted = False
        with (directory / "helper.log").open("w+") as log:
            process = subprocess.Popen(
                [str(Path(binary).resolve()), "-f", str(mountpoint)],
                stdout=log, stderr=log, env={**os.environ, "LC_ALL": "C"})
            try:
                deadline = time.monotonic() + 60
                while time.monotonic() < deadline:
                    if os.path.ismount(mountpoint):
                        mounted = True
                        break
                    if process.poll() is not None:
                        break
                    time.sleep(0.1)
                if mounted:
                    assert (mountpoint / "hello").read_bytes() == b"Hello World!\n"
                    subprocess.run(["fusermount3", "-u", str(mountpoint)],
                                   check=True, timeout=60)
                    mounted = False
                    assert process.wait(timeout=60) == 0
                    print("PASS: independent FUSE 3 host mount probe", flush=True)
                    return 0
                if process.poll() is None:
                    raise RuntimeError("FUSE 3 host probe timed out")
                log.seek(0)
                message = log.read()
                print(message, end="", flush=True)
                # Only established host permission restrictions permit a skip.
                # Missing libraries, crashes and other errors remain failures.
                if ("fusermount3: mount failed: Operation not permitted" in message
                        or "fuse: failed to open /dev/fuse: Permission denied" in message):
                    print("SKIP: independent FUSE 3 mount denied by host", flush=True)
                    for line in Path("/proc/self/status").read_text().splitlines():
                        if line.startswith(("CapEff:", "NoNewPrivs:", "Seccomp:")):
                            print(line, flush=True)
                    return 77
                raise RuntimeError(f"FUSE 3 host probe failed: {process.returncode}")
            finally:
                try:
                    if mounted:
                        subprocess.run(["fusermount3", "-u", str(mountpoint)],
                                       check=True, timeout=60)
                finally:
                    if process.poll() is None:
                        process.kill()
                        process.wait()


def test_payload():
    import guestfs
    import libguestfsmod

    # During RPM checks ensure neither import came from the build source tree.
    if os.environ.get("PYTHONPATH"):
        installed = Path(os.environ["PYTHONPATH"]).resolve()
        for module in (guestfs, libguestfsmod):
            assert Path(module.__file__).resolve().is_relative_to(installed), module.__file__
    print("Python module:", guestfs.__file__, flush=True)
    print("Python extension:", libguestfsmod.__file__, flush=True)

    with tempfile.TemporaryDirectory(prefix="libguestfs-bindings-") as temporary:
        directory = Path(temporary)
        image = directory / "disk.img"
        g = guestfs.GuestFS()
        try:
            g.disk_create(str(image), "raw", 256 * 1024 * 1024)
        finally:
            g.close()
        with handle(image) as g:
            g.part_disk("/dev/sda", "mbr")
            g.mkfs("ext4", "/dev/sda1")
            g.mount("/dev/sda1", "/")
            g.write("/python-test", b"written through Python\n")
            g.sync()

        fuse_available = os.environ.get("OPENRUYI_SKIP_HOST_FUSE") != "1"
        if fuse_available:
            mountpoint = directory / "mount"
            mountpoint.mkdir()
            with host_mount(image, mountpoint):
                assert (mountpoint / "python-test").read_bytes() == b"written through Python\n"
                (mountpoint / "fuse-test").write_bytes(b"written through FUSE\n")
            with host_mount(image, mountpoint, readonly=True):
                assert (mountpoint / "fuse-test").read_bytes() == b"written through FUSE\n"
                try:
                    (mountpoint / "should-not-exist").write_bytes(b"read-only")
                except OSError as error:
                    assert error.errno == errno.EROFS, error
                else:
                    raise AssertionError("read-only guestmount accepted a write")
            print("PASS: guestmount write, unmount, read-only remount and write rejection", flush=True)
        else:
            print("SKIP: host FUSE mount test; independent FUSE 3 probe found host restriction", flush=True)

        with handle(image, readonly=True) as g:
            g.mount_ro("/dev/sda1", "/")
            assert g.read_file("/python-test") == b"written through Python\n"
            if fuse_available:
                assert g.read_file("/fuse-test") == b"written through FUSE\n"
        print("PASS: Python create, write, shutdown and read-only reopen", flush=True)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--probe-host":
        sys.exit(probe_host(sys.argv[2]))
    if len(sys.argv) != 1:
        raise SystemExit("usage: test-python-fuse.py [--probe-host FUSE3_HELLO]")
    test_payload()
