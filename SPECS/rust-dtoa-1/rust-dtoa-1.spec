# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dtoa
%global full_version 1.0.11
%global pkgname dtoa-1

Name:           rust-dtoa-1
Version:        1.0.11
Release:        %autorelease
Summary:        Rust crate "dtoa"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/dtoa
#!RemoteAsset:  sha256:4c3cf4824e2d5f025c7b531afcb2325364084a16806f6d47fbc1f5fbd9960590
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dtoa"

%package     -n %{name}+no-panic
Summary:        Fast floating point primitive to string conversion - feature "no-panic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(no-panic-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/no-panic) = %{version}

%description -n %{name}+no-panic
This metapackage enables feature "no-panic" for the Rust dtoa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
