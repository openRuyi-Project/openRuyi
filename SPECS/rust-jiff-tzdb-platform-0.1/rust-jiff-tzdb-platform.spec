# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jiff-tzdb-platform
%global full_version 0.1.3
%global pkgname jiff-tzdb-platform-0.1

Name:           rust-jiff-tzdb-platform-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "jiff-tzdb-platform"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/jiff/tree/master/crates/jiff-tzdb-platform
#!RemoteAsset:  sha256:875a5a69ac2bab1a891711cf5eccbec1ce0341ea805560dcd90b7a2e925132e8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(jiff-tzdb-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "jiff-tzdb-platform"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
