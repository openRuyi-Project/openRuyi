# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name topological-sort
%global full_version 0.2.2
%global pkgname topological-sort-0.2

Name:           rust-topological-sort-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "topological-sort"
License:        MIT OR Apache-2.0
URL:            https://github.com/gifnksm/topological-sort-rs
#!RemoteAsset:  sha256:ea68304e134ecd095ac6c3574494fc62b909f416c4fca77e440530221e549d3d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "topological-sort"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
