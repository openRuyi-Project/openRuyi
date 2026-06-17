# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fdlimit
%global full_version 0.3.0
%global pkgname fdlimit-0.3

Name:           rust-fdlimit-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "fdlimit"
License:        Apache-2.0
URL:            https://github.com/paritytech/fdlimit
#!RemoteAsset:  sha256:e182f7dbc2ef73d9ef67351c5fbbea084729c48362d3ce9dd44c28e32e277fe5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(thiserror-1/default) >= 1.0.50
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fdlimit"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
