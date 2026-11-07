#!/bin/sh
# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

# Reconstruct the normalized Cargo overlay from flat OBS source files.
set -eu
input_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
output_dir=$(realpath -m -- "${1:?Usage: regenerate.sh OUTPUT_DIRECTORY}")
temporary_dir=$(mktemp -d)
trap 'rm -rf -- "$temporary_dir"' EXIT HUP INT TERM
mkdir -p "$temporary_dir/takopack-overlay/patches"
cp "$input_dir/takopack.toml" "$temporary_dir/takopack.toml"
cp "$input_dir/takopack-series" "$temporary_dir/takopack-overlay/patches/series"
cp "$input_dir/takopack-dependency.patch"     "$temporary_dir/takopack-overlay/patches/2000-Use-a-versioned-compatible-dependency.patch"
cd "$temporary_dir"
takopack cargo pkg serde_macros 0.4.4 --with-spdx --directory "$output_dir"
