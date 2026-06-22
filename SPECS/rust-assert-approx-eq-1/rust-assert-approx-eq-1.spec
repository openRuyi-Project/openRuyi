# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name assert_approx_eq
%global full_version 1.1.0
%global pkgname assert-approx-eq-1

Name:           rust-assert-approx-eq-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "assert_approx_eq"
License:        MIT OR Apache-2.0
URL:            https://github.com/ashleygwilliams/assert_approx_eq.git
#!RemoteAsset:  sha256:3c07dab4369547dbe5114677b33fbbf724971019f3818172d59a97a61c774ffd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "assert_approx_eq"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
