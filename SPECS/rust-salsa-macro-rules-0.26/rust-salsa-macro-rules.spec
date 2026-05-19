# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name salsa-macro-rules
%global full_version 0.26.2
%global pkgname salsa-macro-rules-0.26

Name:           rust-salsa-macro-rules-0.26
Version:        0.26.2
Release:        %autorelease
Summary:        Rust crate "salsa-macro-rules"
License:        Apache-2.0 OR MIT
URL:            https://github.com/salsa-rs/salsa
#!RemoteAsset:  sha256:58e354cbac6939b9b09cd9c11fb419a53e64b4a0f755d929f56a09f4cc752e41
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/accumulator)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "salsa-macro-rules"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
