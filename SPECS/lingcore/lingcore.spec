# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lingcore
%global full_version 0.2.0

# Full integration tests require a Linux host with accessible KVM.
%bcond kvm_tests 0

Name:           lingcore
Version:        0.2.0
Release:        %autorelease
Summary:        Minimal KVM virtual machine monitor
License:        Apache-2.0 AND BSD-3-Clause AND 0BSD AND MIT AND Unicode-3.0
URL:            https://lingcage.com
VCS:            git:https://github.com/RuoqingHe/lingcage.git
#!RemoteAsset:  sha256:a813a741ec85e08e4bf187820a7d961c5ec8440ab4e3f7391c6ca2a88a465d91
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
Source1:        THIRD-PARTY-LICENSES.txt
ExclusiveArch:  x86_64 aarch64 riscv64
BuildSystem:    rust

BuildOption(build):  --no-default-features --features cli --bins

BuildRequires:  rust >= 1.91
BuildRequires:  rust-rpm-macros >= 0.5
BuildRequires:  crate(acpi-tables-0.2/default) >= 0.2.1
BuildRequires:  crate(kvm-bindings-0.14/default) >= 0.14.1
BuildRequires:  crate(kvm-ioctls-0.25/default) >= 0.25.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.180
BuildRequires:  crate(linux-loader-0.14/bzimage) >= 0.14.0
BuildRequires:  crate(log-0.4/default) >= 0.4.29
BuildRequires:  crate(seccompiler-0.5/default) >= 0.5.0
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.149
BuildRequires:  crate(smoltcp-0.13/auto-icmp-echo-reply) >= 0.13.1
BuildRequires:  crate(smoltcp-0.13/medium-ethernet) >= 0.13.1
BuildRequires:  crate(smoltcp-0.13/proto-dhcpv4) >= 0.13.1
BuildRequires:  crate(smoltcp-0.13/proto-ipv4) >= 0.13.1
BuildRequires:  crate(smoltcp-0.13/socket-tcp) >= 0.13.1
BuildRequires:  crate(smoltcp-0.13/socket-udp) >= 0.13.1
BuildRequires:  crate(smoltcp-0.13/std) >= 0.13.1
BuildRequires:  crate(thiserror-2/default) >= 2.0.18
BuildRequires:  crate(vm-fdt-0.3/default) >= 0.3.0
BuildRequires:  crate(vm-memory-0.18/backend-mmap) >= 0.18.0
BuildRequires:  crate(vm-memory-0.18/default) >= 0.18.0
BuildRequires:  crate(vmm-sys-util-0.15/default) >= 0.15.0

%description
LingCore provides a command-line KVM virtual machine monitor with direct Linux
kernel boot, guest memory, a minimal device model, and snapshot primitives.
Running a guest requires access to /dev/kvm and a separately supplied guest
kernel and root filesystem. RISC-V hosts also require an AIA interrupt controller.

%prep -a
cp %{SOURCE1} THIRD-PARTY-LICENSES.txt

%install
install -Dm0755 target/release/lingcore %{buildroot}%{_bindir}/lingcore

%check
# Compile the full test suite even when the build worker has no KVM device.
cargo test --offline --no-default-features --features cli --no-run
# These tests exercise logging and CLI parsing without opening /dev/kvm.
cargo test --offline --no-default-features --features hv --lib
cargo test --offline --no-default-features --features cli --bin lingcore
target/release/lingcore --help
%if %{with kvm_tests}
cargo test --offline --no-default-features --features cli
%endif

%files
%license LICENSE THIRD-PARTY-LICENSES.txt
%doc README.md CHANGELOG.md
%{_bindir}/lingcore

%changelog
%autochangelog
