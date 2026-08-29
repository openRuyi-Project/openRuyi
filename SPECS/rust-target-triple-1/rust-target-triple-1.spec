# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name target-triple
%global full_version 1.0.0
%global pkgname target-triple-1

Name:           rust-target-triple-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "target-triple"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/target-triple
#!RemoteAsset:  sha256:591ef38edfb78ca4771ee32cf494cb8771944bee237a9b91fc9c1424ac4b777b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "target-triple"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
