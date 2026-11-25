# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name take_mut
%global full_version 0.2.2
%global pkgname take-mut-0.2

Name:           rust-take-mut-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "take_mut"
License:        MIT
URL:            https://github.com/Sgeo/take_mut
#!RemoteAsset:  sha256:f764005d11ee5f36500a149ace24e00e3da98b0158b3e2d53a7495660d3f4d60
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "take_mut"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
