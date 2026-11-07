# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name webpki-roots
%global full_version 0.22.6
%global pkgname webpki-roots-0.22

Name:           rust-webpki-roots-0.22
Version:        0.22.6
Release:        %autorelease
Summary:        Rust crate "webpki-roots"
License:        MPL-2.0
URL:            https://github.com/rustls/webpki-roots
#!RemoteAsset:  sha256:b6c71e40d7d2c34a5106301fb632274ca37242cd0c9d3e64dbece371a40a2d87
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(webpki-0.22/default) >= 0.22.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "webpki-roots"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
