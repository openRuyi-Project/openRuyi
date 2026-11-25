# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name flagset
%global full_version 0.4.7
%global pkgname flagset-0.4

Name:           rust-flagset-0.4
Version:        0.4.7
Release:        %autorelease
Summary:        Rust crate "flagset"
License:        Apache-2.0
URL:            https://github.com/enarx/flagset
#!RemoteAsset:  sha256:b7ac824320a75a52197e8f2d787f6a38b6718bb6897a35142d749af3c0e8f4fe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "flagset"

%package     -n %{name}+serde
Summary:        Data types and a macro for generating enumeration-based bit flags - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/serde-derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust flagset crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
