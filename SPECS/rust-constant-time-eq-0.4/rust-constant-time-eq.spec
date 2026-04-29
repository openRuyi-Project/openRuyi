# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name constant_time_eq
%global full_version 0.4.2
%global pkgname constant-time-eq-0.4

Name:           rust-constant-time-eq-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "constant_time_eq"
License:        CC0-1.0 OR MIT-0 OR Apache-2.0
URL:            https://github.com/cesarb/constant_time_eq
#!RemoteAsset:  sha256:3d52eff69cd5e647efe296129160853a42795992097e8af39800e1060caeea9b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/count-instructions-test)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "constant_time_eq"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
