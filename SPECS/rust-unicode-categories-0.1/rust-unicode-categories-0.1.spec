# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode_categories
%global full_version 0.1.1
%global pkgname unicode-categories-0.1

Name:           rust-unicode-categories-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "unicode_categories"
License:        MIT OR Apache-2.0
URL:            https://github.com/swgillespie/unicode-categories
#!RemoteAsset:  sha256:39ec24b3121d976906ece63c9daad25b85969647682eee313cb5779fdd69e14e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unicode_categories"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
