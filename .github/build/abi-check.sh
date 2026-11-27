#!/usr/bin/env bash
# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Compare the ABI of freshly built RPMs (in cwd, from the build artifact)
# against the currently released RPMs fetched from the openruyi repo.
#
# Requires: abipkgdiff (libabigail), rpm, dnf5 (dnf download)
#
# By default ABI changes are only reported as warnings (GitHub Actions
# ::warning:: annotations) and never fail the CI.  Set ABI_CHECK_STRICT=1
# to fail the CI on incompatible ABI changes instead.
#
# Exit codes:
#   0: no incompatible ABI change (or not in strict mode)
#   1: at least one incompatible ABI change and ABI_CHECK_STRICT=1
#   2: tooling/usage error
set -Eeuo pipefail

STRICT="${ABI_CHECK_STRICT:-0}"

REPO_URL="${REPO_URL:-https://repo.build.openruyi.cn/openruyi/x86_64/}"
WORKDIR="${ABI_WORKDIR:-$(mktemp -d)}"
mkdir -p "$WORKDIR/old" "$WORKDIR/new"

NEW_RPMS=()
while IFS= read -r -d '' f; do
    case "$f" in
        *.src.rpm) ;;                       # skip source packages
        *-debuginfo-*) ;;                   # debuginfo is used as debug info, not compared standalone
        *)         NEW_RPMS+=("$f") ;;
    esac
done < <(find . -maxdepth 1 -name '*.rpm' -print0)

if [ "${#NEW_RPMS[@]}" -eq 0 ]; then
    echo "abi-check: no built rpm found in $(pwd)"
    exit 2
fi

FAILED=0
SKIPPED=0

for new in "${NEW_RPMS[@]}"; do
    nvr="$(rpm -qp --qf '%{NAME}-%{VERSION}-%{RELEASE}' "$new")"
    name="$(rpm -qp --qf '%{NAME}' "$new")"
    echo "=== abi-check: $nvr ==="

    # Fetch the released old version of the same package name from the repo.
    # (dnf5 download has no --downloadonly: it errors out if the package does
    #  not exist in the repo, which is exactly what we rely on for new packages)
    if ! dnf download --destdir="$WORKDIR/old" "$name" >/dev/null 2>&1; then
        echo "  new package, no released version in repo, skip."
        SKIPPED=$((SKIPPED + 1))
        continue
    fi
    old="$(find "$WORKDIR/old" -maxdepth 1 -name "$name-[0-9]*.rpm" ! -name '*.src.rpm' | head -n1)"
    if [ -z "$old" ]; then
        echo "  new package, no released version in repo, skip."
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # debuginfo package; fetch old if available (best-effort)
    old_dbg="$(find "$WORKDIR/old" -maxdepth 1 -name "$name-debuginfo-*.rpm" | head -n1 || true)"
    if [ -z "$old_dbg" ]; then
        dnf download --destdir="$WORKDIR/old" "$name-debuginfo" >/dev/null 2>&1 || true
        old_dbg="$(find "$WORKDIR/old" -maxdepth 1 -name "$name-debuginfo-*.rpm" | head -n1 || true)"
    fi
    new_dbg="$(find . -maxdepth 1 -name "$name-debuginfo-*.rpm" | head -n1 || true)"

    args=()
    if [ -n "$old_dbg" ]; then args+=(--debug-info-pkg1 "$old_dbg"); fi
    if [ -n "$new_dbg" ]; then args+=(--debug-info-pkg2 "$new_dbg"); fi
    args+=(--dso-only)

    echo "  comparing: $old"
    echo "           vs $new"
    # Capture output and exit status of abipkgdiff in a single shot
    set +e
    output="$(abipkgdiff "${args[@]}" "$old" "$new" 2>&1)"
    rc=$?
    set -e
    echo "$output"
    if [ "$rc" -eq 127 ]; then
        # command not found
        echo "  ERROR: abipkgdiff not found, cannot check ABI"
        exit 2
    fi
    # ABIDIFF_ABI_INCOMPATIBLE_CHANGE is bit 3 (value 8)
    if [ $((rc & 8)) -ne 0 ]; then
        echo "  WARN: incompatible ABI change detected in $name"
        if [ "$STRICT" -eq 1 ]; then
            echo "::error::abi-check: incompatible ABI change detected in $name ($nvr)"
            FAILED=$((FAILED + 1))
        else
            echo "::warning::abi-check: incompatible ABI change detected in $name ($nvr)"
        fi
    elif [ "$rc" -ne 0 ]; then
        echo "  WARN: ABI changed but considered compatible (exit $rc)"
        echo "::notice::abi-check: compatible ABI change in $name ($nvr) (exit $rc)"
    else
        echo "  OK: ABI unchanged"
    fi
done

echo "=== abi-check summary: $FAILED failed, $SKIPPED skipped ==="
if [ "$FAILED" -ne 0 ]; then
    exit 1
fi
exit 0
