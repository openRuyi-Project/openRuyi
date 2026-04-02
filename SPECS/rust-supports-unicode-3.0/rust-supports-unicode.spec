# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name supports-unicode
%global full_version 3.0.0
%global pkgname supports-unicode-3.0

Name:           rust-supports-unicode-3.0
Version:        3.0.0
Release:        %autorelease
Summary:        Rust crate "supports-unicode"
License:        Apache-2.0
URL:            https://github.com/zkat/supports-unicode
#!RemoteAsset:  sha256:b7401a30af6cb5818bb64852270bb722533397edcfc7344954a38f420819ece2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "supports-unicode"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
