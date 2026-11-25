# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name include_dir_macros
%global full_version 0.7.4
%global pkgname include-dir-macros-0.7

Name:           rust-include-dir-macros-0.7
Version:        0.7.4
Release:        %autorelease
Summary:        Rust crate "include_dir_macros"
License:        MIT
URL:            https://github.com/Michael-F-Bryan/include_dir
#!RemoteAsset:  sha256:7cab85a7ed0bd5f0e76d93846e0147172bed2e2d3f859bcc33a8d9699cad1a75
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/metadata) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "include_dir_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
