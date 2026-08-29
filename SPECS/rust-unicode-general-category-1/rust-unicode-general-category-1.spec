# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-general-category
%global full_version 1.1.0
%global pkgname unicode-general-category-1

Name:           rust-unicode-general-category-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "unicode-general-category"
License:        Apache-2.0
URL:            https://github.com/yeslogic/unicode-general-category
#!RemoteAsset:  sha256:0b993bddc193ae5bd0d623b49ec06ac3e9312875fdae725a975c51db1cc1677f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unicode-general-category"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
