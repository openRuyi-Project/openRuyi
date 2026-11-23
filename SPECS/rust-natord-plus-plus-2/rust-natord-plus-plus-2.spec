# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name natord-plus-plus
%global full_version 2.0.0
%global pkgname natord-plus-plus-2

Name:           rust-natord-plus-plus-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "natord-plus-plus"
License:        MIT
URL:            https://github.com/lifthrasiir/rust-natord
#!RemoteAsset:  sha256:66f8ac0a79782d13e4ec2f955113676d786539965b3764e06fb4e107dcc3da64
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "natord-plus-plus"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
