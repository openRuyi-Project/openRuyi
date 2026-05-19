# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libcst_derive
%global full_version 1.8.6
%global pkgname libcst-derive-1.0

Name:           rust-libcst-derive-1.0
Version:        1.8.6
Release:        %autorelease
Summary:        Rust crate "libcst_derive"
License:        MIT
URL:            https://github.com/Instagram/LibCST
#!RemoteAsset:  sha256:0903173ea316c34a44d0497161e04d9210af44f5f5e89bf2f55d9a254c9a0e8d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "libcst_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
