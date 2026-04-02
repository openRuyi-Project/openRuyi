# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name normalize-line-endings
%global full_version 0.3.0
%global pkgname normalize-line-endings-0.3

Name:           rust-normalize-line-endings-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "normalize-line-endings"
License:        Apache-2.0
URL:            https://github.com/derekdreery/normalize-line-endings
#!RemoteAsset:  sha256:61807f77802ff30975e01f4f071c8ba10c022052f98b3294119f3e615d13e5be
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "normalize-line-endings"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
