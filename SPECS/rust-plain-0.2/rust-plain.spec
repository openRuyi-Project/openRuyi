# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name plain
%global full_version 0.2.3
%global pkgname plain-0.2

Name:           rust-plain-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "plain"
License:        MIT/Apache-2.0
URL:            https://github.com/randomites/plain
#!RemoteAsset:  sha256:b4596b6d070b27117e987119b4dac604f3c58cfb0b191112e24771b2faeac1a6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "plain"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
