# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-native-certs
%global full_version 0.8.1
%global pkgname rustls-native-certs-0.8

Name:           rust-rustls-native-certs-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "rustls-native-certs"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/rustls/rustls-native-certs
#!RemoteAsset:  sha256:7fcff2dd52b58a8d98a70243663a0d234c4e2b79235637849d15913394a247d3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(openssl-probe-0.1/default) >= 0.1.2
Requires:       crate(rustls-pki-types-1/default) >= 1.10.0
Requires:       crate(rustls-pki-types-1/std) >= 1.10.0
Requires:       crate(schannel-0.1/default) >= 0.1.0
Requires:       crate(security-framework-3/default) >= 3.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rustls-native-certs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
