# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lebe
%global full_version 0.5.3
%global pkgname lebe-0.5

Name:           rust-lebe-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "lebe"
License:        BSD-3-Clause
URL:            https://github.com/johannesvollmer/lebe
#!RemoteAsset:  sha256:7a79a3332a6609480d7d0c9eab957bca6b455b91bb84e66d19f5ff66294b85b8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lebe"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
