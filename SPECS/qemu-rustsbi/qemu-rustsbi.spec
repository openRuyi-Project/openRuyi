# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit f16c20d769a30d057b70009089f1277266f7bccd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           qemu-rustsbi
Version:        0.4.1+git20261008.%{shortcommit}
Release:        %autorelease
Summary:        SBI firmware for QEMU RISC-V virtual machines
License:        MIT AND ISC AND MPL-2.0 AND (Apache-2.0 WITH LLVM-exception) AND Unicode-3.0
URL:            https://github.com/rustsbi/rustsbi
#!RemoteAsset:  sha256:1a93eec2f2da4ce7070f644a99ee0a35bd73bb75e9a3a5082bc1dde9245183cd
Source0:        %{url}/archive/%{commit}.tar.gz#/rustsbi-%{commit}.tar.gz
# riscv and riscv-types omit the shared MIT license from their crate archives.
#!RemoteAsset:  sha256:ebe70466a8b881a28612658fad30184d239b07cfb2c5948392d818a28ca3efbc
Source1:        https://raw.githubusercontent.com/rust-embedded/riscv/87d67cf154589cb43f7b56f8a9d5909c72826c52/LICENSE-MIT.md#/riscv-LICENSE-MIT
BuildArch:      noarch
BuildSystem:    rust

# Distribution-only workspace/tool selection; retain the upstream firmware builder.
# https://github.com/rustsbi/rustsbi/tree/f16c20d769a30d057b70009089f1277266f7bccd/xtask
Patch2000:      2000-use-distribution-build-tools.patch

BuildOption(build):  --package xtask

# The rust package includes rust-src; upstream rebuilds core and alloc.
BuildRequires:  rust >= 1.97.1
BuildRequires:  rust-rpm-macros >= 0.5
BuildRequires:  llvm
BuildRequires:  lld
# build-std resolves proc_macro and its dependencies from the Rust 1.97.1 sysroot.
BuildRequires:  crate(rustc-literal-escaper-0.0.7/rustc-dep-of-std) >= 0.0.7
# Keep the exact versions pinned by the sysroot library/Cargo.lock available
# in the distribution registry.
BuildRequires:  crate(hashbrown-0.17/rustc-dep-of-std) >= 0.17.1
BuildRequires:  crate(libc-0.2.185/rustc-dep-of-std) >= 0.2.185
BuildRequires:  crate(memchr-2.7.6/rustc-dep-of-std) >= 2.7.6
# Derived from the external dependencies in the patched workspace with
# `cargo metadata --no-deps --format-version 1`; feature-specific crate
# provides and the xtask test dependencies are included below. Re-run that
# command after changing the workspace members or dependency declarations.
BuildRequires:  crate(anyhow-1/default) >= 1.0.89
BuildRequires:  crate(assert-cmd-2/default) >= 2.0.0
BuildRequires:  crate(bitflags-2/default) >= 2.11.1
BuildRequires:  crate(cfg-if-1/default) >= 1.0.0
BuildRequires:  crate(clap-4/default) >= 4.5.4
BuildRequires:  crate(clap-4/derive) >= 4.5.4
BuildRequires:  crate(clap-4/suggestions) >= 4.5.4
BuildRequires:  crate(clap-verbosity-flag-3/default) >= 3.0.2
BuildRequires:  crate(fdt-0.1/default) >= 0.1.5
BuildRequires:  crate(log-0.4/default) >= 0.4.21
BuildRequires:  crate(memoffset-0.9/default) >= 0.9.1
BuildRequires:  crate(panic-halt-1/default) >= 1.0.0
BuildRequires:  crate(pastey-0.1/default) >= 0.1.0
BuildRequires:  crate(proc-macro2-1/default) >= 1.0.82
BuildRequires:  crate(quote-1/default) >= 1.0.33
BuildRequires:  crate(riscv-0.16) >= 0.16.1
BuildRequires:  crate(riscv-decode-0.2/default) >= 0.2.1
BuildRequires:  crate(seq-macro-0.3/default) >= 0.3.5
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(spin-0.9/default) >= 0.9.8
BuildRequires:  crate(static-assertions-1/default) >= 1.1.0
BuildRequires:  crate(static-toml-1/default) >= 1.0.0
BuildRequires:  crate(syn-2/default) >= 2.0.39
BuildRequires:  crate(syn-2/full) >= 2.0.39
BuildRequires:  crate(tempfile-3/default) >= 3.0.0
BuildRequires:  crate(toml-0.8/default) >= 0.8.20
BuildRequires:  crate(volatile-register-0.2/default) >= 0.2.2

# qemu-system includes both emulators and searches qemu-firmware first.
Requires:       qemu-system >= 11.0.1

%description
This package installs RustSBI as SBI firmware for QEMU RISC-V virtual machines.
It builds dynamic firmware for RV32 and RV64 virt machines from source, with
support for up to eight harts. Firmware is installed in QEMU's priority search
directory; removing this package restores the default firmware search result.

The MPL-covered Flattened Device Tree parser source is available at
https://crates.io/crates/fdt/0.1.5.

%build -p
export CARGO_NET_OFFLINE=true

%build -a
# rust-rpm-macros refreshes Cargo.lock offline against the system registry.
# xtask then uses this resolved lock for both firmware builds.
export RUSTC_BOOTSTRAP=1
export CARGO_TARGET_RISCV32IMAC_UNKNOWN_NONE_ELF_LINKER=ld.lld
export CARGO_TARGET_RISCV64GC_UNKNOWN_NONE_ELF_LINKER=ld.lld
# BARNACLE: BUILD-STD SYSROOT DEPENDENCIES AND LOCK CHECKSUMS NEED DISTRIBUTION SUPPORT
# Rust's separate library/Cargo.lock is not refreshed by rust-rpm-macros.
for target in riscv32imac-unknown-none-elf riscv64gc-unknown-none-elf; do
    cargo prototyper build --target "$target" dynamic
done

%install
for bits in 32 64; do
    case $bits in
        32) target=riscv32imac-unknown-none-elf ;;
        64) target=riscv64gc-unknown-none-elf ;;
    esac
    install -Dm0644 target/$target/release/rustsbi-prototyper-dynamic.bin \
        %{buildroot}%{_datadir}/qemu-firmware/opensbi-riscv${bits}-generic-fw_dynamic.bin
done

# Preserve notices for crates used by this build. Keep the registry hierarchy
# so new crates do not require changes to this Spec. Cargo.toml and README
# files cover crates whose archives omit standalone license files.
license_dir=$PWD/third-party-licenses
mkdir -p "$license_dir"
(
    cd %{_datadir}/cargo/registry
    find . -mindepth 2 -maxdepth 3 -type f \
        \( -iname 'license*' -o -iname 'copying*' -o -iname 'notice*' \
        -o -name 'Cargo.toml' -o -iname 'README*' \) \
        -exec cp --parents '{}' "$license_dir/" \;
)
# The riscv and riscv-types READMEs carry ISC notices. The shared MIT text is
# supplied separately because the crates omit it from their archives.
cp %{SOURCE1} third-party-licenses/riscv-LICENSE-MIT
mkdir -p third-party-licenses/rust
for license in MIT Apache-2.0 LLVM-exception Unicode-3.0; do
    cp %{_defaultdocdir}/rust/licenses/$license.txt third-party-licenses/rust/
done
cp -a %{_defaultdocdir}/rust/COPYRIGHT-library.html third-party-licenses/rust/
cp %{_prefix}/lib/rustlib/src/rust/library/compiler-builtins/LICENSE.txt \
    third-party-licenses/rust/compiler-builtins-LICENSE.txt

%check
# Kernel integration tests require rustup, cargo-binutils and additional kernels.
# Run the host-side builder unit tests without those integration tests.
cargo test --offline --locked --release --package xtask --bin xtask
test -s target/riscv32imac-unknown-none-elf/release/rustsbi-prototyper-dynamic.bin
test -s target/riscv64gc-unknown-none-elf/release/rustsbi-prototyper-dynamic.bin

%files
%license LICENSE-MIT LICENSE-MULAN third-party-licenses
%dir %{_datadir}/qemu-firmware
%{_datadir}/qemu-firmware/opensbi-riscv32-generic-fw_dynamic.bin
%{_datadir}/qemu-firmware/opensbi-riscv64-generic-fw_dynamic.bin

%changelog
%autochangelog
