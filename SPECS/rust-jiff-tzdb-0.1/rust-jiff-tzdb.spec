# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jiff-tzdb
%global full_version 0.1.6
%global pkgname jiff-tzdb-0.1

Name:           rust-jiff-tzdb-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "jiff-tzdb"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/jiff/tree/master/crates/jiff-tzdb
#!RemoteAsset:  sha256:c900ef84826f1338a557697dc8fc601df9ca9af4ac137c7fb61d4c6f2dfd3076
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "jiff-tzdb"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
