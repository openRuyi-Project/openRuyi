# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mintex
%global full_version 0.1.4
%global pkgname mintex-0.1

Name:           rust-mintex-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "mintex"
License:        Apache-2.0
URL:            https://github.com/garypen/mintex
#!RemoteAsset:  sha256:c505b3e17ed6b70a7ed2e67fbb2c560ee327353556120d6e72f5232b6880d536
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mintex"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
