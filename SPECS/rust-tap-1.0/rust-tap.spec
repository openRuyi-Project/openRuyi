# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tap
%global full_version 1.0.1
%global pkgname tap-1.0

Name:           rust-tap-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "tap"
License:        MIT
URL:            https://github.com/myrrlyn/tap
#!RemoteAsset:  sha256:55937e1799185b12863d447f42597ed69d9928686b8d88a1df17376a097d8369
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tap"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
