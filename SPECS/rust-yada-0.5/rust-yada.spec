# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yada
%global full_version 0.5.1
%global pkgname yada-0.5

Name:           rust-yada-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "yada"
License:        MIT OR Apache-2.0
URL:            https://github.com/takuyaa/yada
#!RemoteAsset:  sha256:aed111bd9e48a802518765906cbdadf0b45afb72b9c81ab049a3b86252adffdd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "yada"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
