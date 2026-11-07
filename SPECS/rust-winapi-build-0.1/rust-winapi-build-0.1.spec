# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winapi-build
%global full_version 0.1.1
%global pkgname winapi-build-0.1

Name:           rust-winapi-build-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "winapi-build"
License:        MIT
URL:            https://github.com/retep998/winapi-rs
#!RemoteAsset:  sha256:2d315eee3b34aca4797b2da6b13ed88266e6d612562a0c46390af8299fc699bc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "winapi-build"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
