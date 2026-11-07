# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name webpki-roots
%global full_version 0.21.1
%global pkgname webpki-roots-0.21

Name:           rust-webpki-roots-0.21
Version:        0.21.1
Release:        %autorelease
Summary:        Rust crate "webpki-roots"
License:        MPL-2.0
URL:            https://github.com/ctz/webpki-roots
#!RemoteAsset:  sha256:aabe153544e473b775453675851ecc86863d2a81d786d741f6b76778f2a48940
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(webpki-0.21/default) >= 0.21.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "webpki-roots"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
