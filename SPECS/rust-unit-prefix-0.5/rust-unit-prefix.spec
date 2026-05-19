# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unit-prefix
%global full_version 0.5.1
%global pkgname unit-prefix-0.5

Name:           rust-unit-prefix-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "unit-prefix"
License:        MIT
URL:            https://github.com/commons-rs/unit-prefix
#!RemoteAsset:  sha256:323402cff2dd658f39ca17c789b502021b3f18707c91cdf22e3838e1b4023817
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "unit-prefix"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
