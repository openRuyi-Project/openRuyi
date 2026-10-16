# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cargo-packaging
Version:        1.5.0
Release:        %autorelease
Summary:        Cargo packaging macros and Rust RPM dependency generator
License:        MPL-2.0
URL:            https://github.com/openSUSE-Rust/cargo-packaging
#!RemoteAsset:  sha256:0ce497900c113bd72cad2d9979d4a33ef88858328c4f5dcea05f1dd1b0c618b9
Source0:        https://github.com/openSUSE-Rust/cargo-packaging/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  cargo-auditable
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(auditable-info-0.6/default) >= 0.6.2
BuildRequires:  crate(clap-3/default) >= 3.2.0
BuildRequires:  crate(clap-3/derive) >= 3.2.0
BuildRequires:  crate(clap-3/env) >= 3.2.0
BuildRequires:  crate(clap-complete-3/default) >= 3.2.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.35
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.14
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.14
BuildRequires:  crate(tracing-subscriber-0.3/fmt) >= 0.3.14

Requires:       cargo
Requires:       cargo-auditable
Requires:       rust
Requires:       rpm-build

%description
Cargo packaging macros provide build, test, and install helpers for Rust
applications. The Rust RPM dependency generator extracts embedded Cargo
dependency metadata from auditable binaries and exposes bundled crate versions
to RPM.

%build -p
export CARGO="cargo auditable"

%install
install -Dm0755 target/release/rust-rpm-prov %{buildroot}%{_rpmconfigdir}/rust-rpm-prov
install -Dm0644 macros.cargo %{buildroot}%{_rpmmacrodir}/macros.cargo
install -Dm0644 rust.attr %{buildroot}%{_rpmconfigdir}/fileattrs/rust.attr
install -Dm0644 target/release/build/completions/rust-rpm-prov.bash %{buildroot}%{bash_completions_dir}/rust-rpm-prov
install -Dm0644 target/release/build/completions/_rust-rpm-prov %{buildroot}%{_datadir}/zsh/site-functions/_rust-rpm-prov

%check -a
target/release/rust-rpm-prov --help
printf '%s\n' /bin/true | target/release/rust-rpm-prov rpm-provides > provides.txt
test ! -s provides.txt
printf '%s\n' "$PWD/target/release/rust-rpm-prov" | target/release/rust-rpm-prov rpm-provides > rust-provides.txt
grep -Fx 'bundled(rust-crate:rust-rpm-prov) = 0.1.0' rust-provides.txt
grep -F 'bundled(rust-crate:auditable-info) = 0.6.2' rust-provides.txt

%files
%doc README.md
%license LICENSE.md
%{_rpmconfigdir}/rust-rpm-prov
%{_rpmconfigdir}/fileattrs/rust.attr
%{_rpmmacrodir}/macros.cargo
%{bash_completions_dir}/rust-rpm-prov
%{_datadir}/zsh/site-functions/_rust-rpm-prov

%changelog
%autochangelog
