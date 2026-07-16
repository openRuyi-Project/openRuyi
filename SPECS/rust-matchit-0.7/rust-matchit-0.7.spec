# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name matchit
%global full_version 0.7.3
%global pkgname matchit-0.7

Name:           rust-matchit-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "matchit"
License:        MIT AND BSD-3-Clause
URL:            https://github.com/ibraheemdev/matchit
#!RemoteAsset:  sha256:0e7465ac9959cc2b1404e8e2367b43684a6d13790fe23056cc8c6c5a6b7bcb94
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/test-helpers) = %{version}

%description
Source code for takopackized Rust crate "matchit"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
