# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitmaps
%global full_version 2.1.0
%global pkgname bitmaps-2.0

Name:           rust-bitmaps-2.0
Version:        2.1.0
Release:        %autorelease
Summary:        Rust crate "bitmaps"
License:        MPL-2.0+
URL:            https://github.com/bodil/bitmaps
#!RemoteAsset:  sha256:031043d04099746d8db04daf1fa424b2bc8bd69d92b25962dcde24da39ab64a2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(typenum-1.0/default) >= 1.19.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "bitmaps"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
