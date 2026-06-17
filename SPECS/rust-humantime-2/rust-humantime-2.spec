# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name humantime
%global full_version 2.3.0
%global pkgname humantime-2

Name:           rust-humantime-2
Version:        2.3.0
Release:        %autorelease
Summary:        Rust crate "humantime"
License:        MIT OR Apache-2.0
URL:            https://github.com/chronotope/humantime
#!RemoteAsset:  sha256:135b12329e5e3ce057a9f972339ea52bc954fe1e9358ef27f95e89716fbc5424
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/mu) = %{version}

%description
Source code for takopackized Rust crate "humantime"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
