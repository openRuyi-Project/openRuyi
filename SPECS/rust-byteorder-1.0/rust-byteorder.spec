# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name byteorder
%global full_version 1.5.0
%global pkgname byteorder-1.0

Name:           rust-byteorder-1.0
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "byteorder"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/byteorder
#!RemoteAsset:  sha256:1fd0f2584146f6f2ef48085050886acf353beff7305ebd1ae69500e27c67f64b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/i128)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "byteorder"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
