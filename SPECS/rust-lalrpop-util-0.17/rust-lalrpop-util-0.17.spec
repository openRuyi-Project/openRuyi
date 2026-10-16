# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lalrpop-util
%global full_version 0.17.2
%global pkgname lalrpop-util-0.17

Name:           rust-lalrpop-util-0.17
Version:        0.17.2
Release:        %autorelease
Summary:        Rust crate "lalrpop-util"
License:        Apache-2.0 OR MIT
URL:            https://github.com/lalrpop/lalrpop
#!RemoteAsset:  sha256:c277d18683b36349ab5cd030158b54856fca6bb2d5dc5263b06288f486958b7c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lalrpop-util"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
