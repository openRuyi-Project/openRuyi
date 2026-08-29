# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name matches
%global full_version 0.1.10
%global pkgname matches-0.1

Name:           rust-matches-0.1
Version:        0.1.10
Release:        %autorelease
Summary:        Rust crate "matches"
License:        MIT
URL:            https://github.com/SimonSapin/rust-std-candidates
#!RemoteAsset:  sha256:2532096657941c2fea9c289d370a250971c689d4f143798ff67113ec042024a5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "matches"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
