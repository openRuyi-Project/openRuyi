# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memo-map
%global full_version 0.3.3
%global pkgname memo-map-0.3

Name:           rust-memo-map-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "memo-map"
License:        Apache-2.0
URL:            https://github.com/mitsuhiko/memo-map
#!RemoteAsset:  sha256:38d1115007560874e373613744c6fba374c17688327a71c1476d1a5954cc857b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "memo-map"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
