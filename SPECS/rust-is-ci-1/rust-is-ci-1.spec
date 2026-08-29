# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name is_ci
%global full_version 1.2.0
%global pkgname is-ci-1

Name:           rust-is-ci-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "is_ci"
License:        ISC
URL:            https://github.com/zkat/is_ci
#!RemoteAsset:  sha256:7655c9839580ee829dfacba1d1278c2b7883e50a277ff7541299489d6bdfdc45
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Just tells you if you're in CI or not without much fuss.
Source code for takopackized Rust crate "is_ci"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
