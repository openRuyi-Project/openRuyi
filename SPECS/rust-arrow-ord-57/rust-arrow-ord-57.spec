# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-ord
%global full_version 57.3.1
%global pkgname arrow-ord-57

Name:           rust-arrow-ord-57
Version:        57.3.1
Release:        %autorelease
Summary:        Rust crate "arrow-ord"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:082342947d4e5a2bcccf029a0a0397e21cb3bb8421edd9571d34fb5dd2670256
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-57/default) >= 57.3.1
Requires:       crate(arrow-buffer-57/default) >= 57.3.1
Requires:       crate(arrow-data-57/default) >= 57.3.1
Requires:       crate(arrow-schema-57/default) >= 57.3.1
Requires:       crate(arrow-select-57/default) >= 57.3.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-ord"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
