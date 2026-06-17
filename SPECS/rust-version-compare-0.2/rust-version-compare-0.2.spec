# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name version-compare
%global full_version 0.2.1
%global pkgname version-compare-0.2

Name:           rust-version-compare-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "version-compare"
License:        MIT
URL:            https://timvisee.com/projects/version-compare/
#!RemoteAsset:  sha256:03c2856837ef78f57382f06b2b8563a2f512f7185d732608fd9176cb3b8edf0e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "version-compare"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
