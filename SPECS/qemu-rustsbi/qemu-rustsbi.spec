# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

Name:           qemu-rustsbi
Version:        0.4.1^20261008gitf16c20d
Release:        %autorelease
Summary:        RustSBI firmware for QEMU RISC-V virtual machines
License:        MIT AND MPL-2.0 AND (Apache-2.0 WITH LLVM-exception) AND Unicode-3.0
URL:            https://github.com/rustsbi/rustsbi
# Prebuilt from RustSBI f16c20d769a30d057b70009089f1277266f7bccd.
# Built with Rust/rust-src 1.97.1, RUSTC_BOOTSTRAP=1 and LLVM/LLD 22.1.6.
# Targets: riscv32imac-unknown-none-elf and riscv64gc-unknown-none-elf.
Source0:        rustsbi-riscv32-dynamic.bin
Source1:        rustsbi-riscv64-dynamic.bin
Source2:        LICENSE-MIT
Source3:        ThirdPartyNotices.txt
BuildArch:      noarch

# This RPM includes both RISC-V emulators and searches qemu-firmware first.
Requires:       qemu-system >= 11.0.1

%description
This package provides RustSBI as SBI firmware for QEMU RISC-V virtual machines.
It installs prebuilt dynamic firmware for RV32 and RV64 virt machines, with
support for up to eight harts.

Unmodified source: https://github.com/rustsbi/rustsbi/tree/f16c20d769a30d057b70009089f1277266f7bccd
MPL-covered fdt source: https://crates.io/crates/fdt/0.1.5

%prep
%setup -q -c -T
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .
sha256sum --check <<'EOF'
d2bcb01355763b1e857e7715992d68987e98a2fc5d740fc2e902679df2ca0588  rustsbi-riscv32-dynamic.bin
b8ee3cfbfe708b62f2e459d866c7c501e623ad239dc2a44bda43afd9e0c37b2e  rustsbi-riscv64-dynamic.bin
EOF

%install
install -d %{buildroot}%{_datadir}/qemu-firmware
install -m 0644 rustsbi-riscv32-dynamic.bin \
    %{buildroot}%{_datadir}/qemu-firmware/opensbi-riscv32-generic-fw_dynamic.bin
install -m 0644 rustsbi-riscv64-dynamic.bin \
    %{buildroot}%{_datadir}/qemu-firmware/opensbi-riscv64-generic-fw_dynamic.bin

%files
%license LICENSE-MIT ThirdPartyNotices.txt
%dir %{_datadir}/qemu-firmware
%{_datadir}/qemu-firmware/opensbi-riscv32-generic-fw_dynamic.bin
%{_datadir}/qemu-firmware/opensbi-riscv64-generic-fw_dynamic.bin

%changelog
%autochangelog
