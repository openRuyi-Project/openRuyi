# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-utils
%global full_version 0.7.2
%global pkgname crossbeam-utils-0.7

Name:           rust-crossbeam-utils-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "crossbeam-utils"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils
#!RemoteAsset:  sha256:c3c7c73a2d1e9fc0886a08b93e98eb643461230d5f1925e4036204d5f2e261a8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(cfg-if-0.1/default) >= 0.1.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "crossbeam-utils"

%package     -n %{name}+lazy-static
Summary:        Utilities for concurrent programming - feature "lazy_static" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lazy-static-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/lazy-static) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust crossbeam-utils crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "std" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
