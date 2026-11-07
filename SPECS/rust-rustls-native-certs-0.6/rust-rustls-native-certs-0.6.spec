# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-native-certs
%global full_version 0.6.3
%global pkgname rustls-native-certs-0.6

Name:           rust-rustls-native-certs-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "rustls-native-certs"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/ctz/rustls-native-certs
#!RemoteAsset:  sha256:a9aace74cb666635c918e9c12bc0d348266037aa8eb599b5cba565709a8dff00
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(openssl-probe-0.1/default) >= 0.1.2
Requires:       crate(rustls-pemfile-1/default) >= 1.0.0
Requires:       crate(schannel-0.1/default) >= 0.1.15
Requires:       crate(security-framework-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rustls-native-certs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
