# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name appendlist
%global full_version 1.4.0
%global pkgname appendlist-1

Name:           rust-appendlist-1
Version:        1.4.0
Release:        %autorelease
Summary:        Rust crate "appendlist"
License:        MIT
URL:            https://github.com/danieldulaney/appendlist
#!RemoteAsset:  sha256:e149dc73cd30538307e7ffa2acd3d2221148eaeed4871f246657b1c3eaa1cbd2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "appendlist"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
