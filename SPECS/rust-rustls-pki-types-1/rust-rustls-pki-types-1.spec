# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-pki-types
%global full_version 1.15.1
%global pkgname rustls-pki-types-1

Name:           rust-rustls-pki-types-1
Version:        1.15.1
Release:        %autorelease
Summary:        Rust crate "rustls-pki-types"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustls/pki-types
#!RemoteAsset:  sha256:2f4925028c7eb5d1fcdaf196971378ed9d2c1c4efc7dc5d011256f76c99c0a96
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rustls-pki-types"

%package     -n %{name}+alloc
Summary:        Shared types for the rustls PKI ecosystem - feature "alloc" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rustls-pki-types crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "std" features.

%package     -n %{name}+web-time
Summary:        Shared types for the rustls PKI ecosystem - feature "web-time" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(web-time-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/web) = %{version}
Provides:       crate(%{pkgname}/web-time) = %{version}

%description -n %{name}+web-time
This metapackage enables feature "web-time" for the Rust rustls-pki-types crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "web" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
