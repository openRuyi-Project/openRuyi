# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name avt
%global full_version 0.17.0
%global pkgname avt-0.17

Name:           rust-avt-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "avt"
License:        Apache-2.0
URL:            https://github.com/asciinema/avt
#!RemoteAsset:  sha256:fa0f99f7bcce0e99d842c94947f8d0ab5f6f3abc08424e1a4b58a8a7ae30f7c7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rgb-0.8/default) >= 0.8.33
Requires:       crate(unicode-width-0.1/default) >= 0.1.13
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "avt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
