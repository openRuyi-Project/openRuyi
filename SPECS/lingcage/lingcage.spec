# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lingcage
%global full_version 0.2.0

# Full integration tests require a Linux host with accessible KVM.
%bcond kvm_tests 0

Name:           lingcage
Version:        0.2.0
Release:        %autorelease
Summary:        Run commands in cloned KVM microVM sandboxes
License:        Apache-2.0 AND BSD-3-Clause AND 0BSD AND MIT AND Unicode-3.0
URL:            https://lingcage.com
VCS:            git:https://github.com/RuoqingHe/lingcage.git
#!RemoteAsset:  sha256:470d09558753474b2f4ecd3eeb4364a0ac91e483700cbf02d362333e0dec88c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
Source1:        README.openRuyi.md
Source2:        THIRD-PARTY-LICENSES.txt
ExclusiveArch:  x86_64 aarch64 riscv64
BuildSystem:    rust

BuildOption(build):  --no-default-features --features cli,agent --bins

BuildRequires:  rust >= 1.91
BuildRequires:  rust-rpm-macros >= 0.5
BuildRequires:  crate(libc-0.2/default) >= 0.2.180
BuildRequires:  crate(lingcore-0.2/default) >= 0.2.0
BuildRequires:  crate(lingcore-0.2/kvm) >= 0.2.0
BuildRequires:  crate(lingcore-0.2/machine) >= 0.2.0
BuildRequires:  crate(log-0.4/default) >= 0.4.29
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.149
BuildRequires:  crate(sha2-0.10/default) >= 0.10.9
BuildRequires:  crate(thiserror-2/default) >= 2.0.18

%description
LingCage creates templates from booted Linux guests and runs commands in cloned
microVM sandboxes. It uses the LingCore Rust library, linked at build time.
Running a sandbox requires access to /dev/kvm, a guest kernel, and a guest image
containing the matching lingcage-agent. RISC-V hosts require an AIA interrupt
controller. The software is under active development.

%package agent
Summary:        Guest-side command execution agent for LingCage

%description agent
The LingCage guest agent connects to the host through virtio-vsock and executes
commands inside a microVM. Install it in the guest image. It does not require
LingCage or access to /dev/kvm inside the guest. The guest image must provide the
shared libraries required by this distribution-built executable.

%prep -a
cp %{SOURCE2} THIRD-PARTY-LICENSES.txt
cp %{SOURCE1} README.openRuyi.md

%install
install -Dm0755 target/release/lingcage %{buildroot}%{_bindir}/lingcage
install -Dm0755 target/release/lingcage-agent %{buildroot}%{_bindir}/lingcage-agent
install -dm0700 %{buildroot}%{_localstatedir}/lib/lingcage

%check
# Compile all host and guest tests, but do not run KVM tests on ordinary workers.
cargo test --offline --no-default-features --features cli,agent --no-run
cargo test --offline --no-default-features --features lcp --lib
cargo test --offline --no-default-features --features cli --bin lingcage
target/release/lingcage --help
# Do not launch lingcage-agent on the build host: it belongs in a guest.
%if %{with kvm_tests}
cargo test --offline --no-default-features --features cli,agent
%endif

%files
%license LICENSE THIRD-PARTY-LICENSES.txt
%doc README.md CHANGELOG.md README.openRuyi.md
%{_bindir}/lingcage
%dir %attr(0700,root,root) %{_localstatedir}/lib/lingcage

%files agent
%license LICENSE THIRD-PARTY-LICENSES.txt
%doc README.openRuyi.md
%{_bindir}/lingcage-agent

%changelog
%autochangelog
