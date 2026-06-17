# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symlink
%global full_version 0.1.0
%global pkgname symlink-0.1

Name:           rust-symlink-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "symlink"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/chris-morgan/symlink
#!RemoteAsset:  sha256:a7973cce6668464ea31f176d85b13c7ab3bba2cb3b77a2ed26abd7801688010a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "symlink"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
