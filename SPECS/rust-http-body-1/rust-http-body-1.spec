# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name http-body
%global full_version 1.1.0
%global pkgname http-body-1

Name:           rust-http-body-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "http-body"
License:        MIT
URL:            https://github.com/hyperium/http-body
#!RemoteAsset:  sha256:ca2a8f2913ee65f60facd6a5905613afaa448497a0230cc41ce022d93290bc2c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(http-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "http-body"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
