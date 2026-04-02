# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name typeid
%global full_version 1.0.3
%global pkgname typeid-1.0

Name:           rust-typeid-1.0
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "typeid"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/typeid
#!RemoteAsset:  sha256:bc7d623258602320d5c55d1bc22793b57daff0ec7efc270ea7d55ce1d5f5471c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "typeid"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
