# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name block
%global full_version 0.1.6
%global pkgname block-0.1

Name:           rust-block-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "block"
License:        MIT
URL:            http://github.com/SSheldon/rust-block
#!RemoteAsset:  sha256:0d8c1fef690941d3e7788d328517591fecc684c084084702d6ff1641e993699a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "block"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
