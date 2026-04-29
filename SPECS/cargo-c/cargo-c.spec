# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-c
%global full_version 0.10.16+cargo-0.91.0

Name:           cargo-c
Version:        0.10.16
Release:        %autorelease
Summary:        Helper program to build and install c-like libraries
License:        MIT
URL:            https://github.com/lu-zero/cargo-c
#!RemoteAsset:  sha256:17d431789b050b0fcf678455dfd5ceb7e5b45cd806140f8fe03b16b995d6cbff
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  pkgconfig(openssl)
BuildRequires:  crate(anyhow-1.0/default) >= 1.0.0
BuildRequires:  crate(cargo-0.91/default) >= 0.91.0
BuildRequires:  crate(openssl-0.10/default) >= 0.10.0
BuildRequires:  crate(openssl-sys-0.9/default) >= 0.9
BuildRequires:  crate(openssl-src-300.0/default) >= 300.5
BuildRequires:  crate(cargo-util-0.2/default) >= 0.2.0
BuildRequires:  crate(cbindgen-0.29) >= 0.29.0
BuildRequires:  crate(cc-1.0/default) >= 1.0.0
BuildRequires:  crate(clap-4.0/cargo) >= 4.5.18
BuildRequires:  crate(clap-4.0/color) >= 4.5.18
BuildRequires:  crate(clap-4.0/default) >= 4.5.18
BuildRequires:  crate(clap-4.0/derive) >= 4.5.18
BuildRequires:  crate(clap-4.0/string) >= 4.5.18
BuildRequires:  crate(clap-4.0/wrap-help) >= 4.5.18
BuildRequires:  crate(glob-0.3/default) >= 0.3.0
BuildRequires:  crate(implib-0.4/default) >= 0.4.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(log-0.4/default) >= 0.4.0
BuildRequires:  crate(object-0.37/pe) >= 0.37.1
BuildRequires:  crate(object-0.37/read-core) >= 0.37.1
BuildRequires:  crate(object-0.37/std) >= 0.37.1
BuildRequires:  crate(regex-1.0/default) >= 1.5.6
BuildRequires:  crate(semver-1.0/default) >= 1.0.3
BuildRequires:  crate(serde-1.0/default) >= 1.0.123
BuildRequires:  crate(serde-derive-1.0/default) >= 1.0.0
BuildRequires:  crate(serde-json-1.0/default) >= 1.0.62
BuildRequires:  crate(toml-0.9/default) >= 0.9.0

%description
cargo applet to build and install C-ABI compatible dynamic and static libraries.
It produces and installs a correct pkg-config file, a static library and a dynamic
library, and a C header to be used by any C (and C-compatible) software.

%install -a
install -Dm0755 target/release/cargo-capi %{buildroot}%{_bindir}/cargo-capi
install -Dm0755 target/release/cargo-cbuild %{buildroot}%{_bindir}/cargo-cbuild
install -Dm0755 target/release/cargo-cinstall %{buildroot}%{_bindir}/cargo-cinstall
install -Dm0755 target/release/cargo-ctest %{buildroot}%{_bindir}/cargo-ctest

%files
%license LICENSE
%{_bindir}/cargo-capi
%{_bindir}/cargo-cbuild
%{_bindir}/cargo-cinstall
%{_bindir}/cargo-ctest
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
