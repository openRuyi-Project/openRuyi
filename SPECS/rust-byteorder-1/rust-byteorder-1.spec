# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name byteorder
%global full_version 1.5.0
%global pkgname byteorder-1

Name:           rust-byteorder-1
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "byteorder"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/byteorder
#!RemoteAsset:  sha256:1fd0f2584146f6f2ef48085050886acf353beff7305ebd1ae69500e27c67f64b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/i128) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "byteorder"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
