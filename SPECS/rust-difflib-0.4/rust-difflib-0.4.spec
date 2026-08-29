# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name difflib
%global full_version 0.4.0
%global pkgname difflib-0.4

Name:           rust-difflib-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "difflib"
License:        MIT
URL:            https://github.com/DimaKudosh/difflib
#!RemoteAsset:  sha256:6184e33543162437515c2e2b48714794e37845ec9851711914eec9d308f6ebe8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "difflib"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
