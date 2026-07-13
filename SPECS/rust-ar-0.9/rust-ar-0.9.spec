# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ar
%global full_version 0.9.0
%global pkgname ar-0.9

Name:           rust-ar-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "ar"
License:        MIT
URL:            https://github.com/mdsteele/rust-ar
#!RemoteAsset:  sha256:d67af77d68a931ecd5cbd8a3b5987d63a1d1d1278f7f6a60ae33db485cdebb69
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ar"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
