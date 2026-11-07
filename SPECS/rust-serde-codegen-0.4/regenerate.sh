#!/bin/sh
# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

# Cargo must read the repaired manifest before it can package this release.
set -eu
input_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
output_dir=$(realpath -m -- "${1:?Usage: regenerate.sh OUTPUT_DIRECTORY}")
temporary_dir=$(mktemp -d)
trap 'rm -rf -- "$temporary_dir"' EXIT HUP INT TERM
cd "$temporary_dir"
curl --fail --location --output archive.crate 'https://static.crates.io/crates/serde_codegen/0.4.3/download'
echo '78039c094484c3f82dd91717644aa922f5372c8ca24b876cc4c8028d377cc704  archive.crate' | sha256sum --check -
mkdir source
tar -xf archive.crate --strip-components=1 -C source
patch -d source -p1 < "$input_dir/2000-Correct-dependency-metadata-for-the-Serde-0.4-generator.patch"
cp "$input_dir/takopack.toml" takopack.toml
takopack cargo pkg serde_codegen 0.4.3 --with-spdx --directory "$output_dir"
