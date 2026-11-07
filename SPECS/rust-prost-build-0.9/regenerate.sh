#!/bin/sh
set -eu
input_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
output_argument=${1:?Usage: regenerate.sh OUTPUT_DIRECTORY}
mkdir -p "$output_argument"
output_dir=$(CDPATH= cd -- "$output_argument" && pwd)
temporary_dir=$(mktemp -d)
trap 'rm -rf -- "$temporary_dir"' EXIT HUP INT TERM
mkdir -p "$temporary_dir/takopack-overlay/patches"
cp "$input_dir/takopack.toml" "$temporary_dir/takopack.toml"
cp "$input_dir/takopack-series" "$temporary_dir/takopack-overlay/patches/series"
cp "$input_dir/2000-Use-the-system-Protobuf-compiler-and-include-directory.patch" "$temporary_dir/takopack-overlay/patches/2000-Use-the-system-Protobuf-compiler-and-include-directory.patch"
cd "$temporary_dir"
takopack cargo pkg prost-build 0.9.0 --with-spdx --directory "$output_dir"

# Keep the review manifest identical to the crate source after its declared patch.
cd "$output_dir/rust-prost-build-0.9"
git apply --allow-empty --include=Cargo.toml "$input_dir/2000-Use-the-system-Protobuf-compiler-and-include-directory.patch"
