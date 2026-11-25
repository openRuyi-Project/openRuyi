# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-row
%global full_version 57.3.1
%global pkgname arrow-row-57

Name:           rust-arrow-row-57
Version:        57.3.1
Release:        %autorelease
Summary:        Rust crate "arrow-row"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:e3a931b520a2a5e22033e01a6f2486b4cdc26f9106b759abeebc320f125e94d7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-57/default) >= 57.3.1
Requires:       crate(arrow-buffer-57/default) >= 57.3.1
Requires:       crate(arrow-data-57/default) >= 57.3.1
Requires:       crate(arrow-schema-57/default) >= 57.3.1
Requires:       crate(half-2) >= 2.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-row"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
