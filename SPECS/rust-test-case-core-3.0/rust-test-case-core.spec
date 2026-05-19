# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name test-case-core
%global full_version 3.3.1
%global pkgname test-case-core-3.0

Name:           rust-test-case-core-3.0
Version:        3.3.1
Release:        %autorelease
Summary:        Rust crate "test-case-core"
License:        MIT
URL:            https://github.com/frondeus/test-case
#!RemoteAsset:  sha256:adcb7fd841cd518e279be3d5a3eb0636409487998a4aff22f3de87b81e88384f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.0
Requires:       crate(proc-macro2-1.0/default) >= 1.0.0
Requires:       crate(quote-1.0/default) >= 1.0.0
Requires:       crate(syn-2.0/default) >= 2.0.0
Requires:       crate(syn-2.0/extra-traits) >= 2.0.0
Requires:       crate(syn-2.0/full) >= 2.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/with-regex)

%description
Source code for takopackized Rust crate "test-case-core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
