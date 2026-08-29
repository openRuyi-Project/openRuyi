# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ident_case
%global full_version 1.0.1
%global pkgname ident-case-1

Name:           rust-ident-case-1
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "ident_case"
License:        MIT OR Apache-2.0
URL:            https://github.com/TedDriggs/ident_case
#!RemoteAsset:  sha256:b9e0384b61958566e926dc50660321d12159025e767c18e043daf26b70104c39
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ident_case"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
