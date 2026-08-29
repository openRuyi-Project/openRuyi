# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name httpdate
%global full_version 1.0.3
%global pkgname httpdate-1

Name:           rust-httpdate-1
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "httpdate"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyfisch/httpdate
#!RemoteAsset:  sha256:df3b46402a9d5adb4c86a0cf463f42e19994e3ee891101b1841f30a545cb49a9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "httpdate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
