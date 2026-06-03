# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name number_prefix
%global full_version 0.4.0
%global pkgname number-prefix-0.4

Name:           rust-number-prefix-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "number_prefix"
License:        MIT
URL:            https://github.com/ogham/rust-number-prefix
#!RemoteAsset:  sha256:830b246a0e5f20af87141b25c173cd1b609bd7779a4617d6ec582abaf90870f3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "number_prefix"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
