# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ordermap
%global full_version 0.3.5
%global pkgname ordermap-0.3

Name:           rust-ordermap-0.3
Version:        0.3.5
Release:        %autorelease
Summary:        Rust crate "ordermap"
License:        Apache-2.0 OR MIT
URL:            https://github.com/bluss/ordermap
#!RemoteAsset:  sha256:a86ed3f5f244b372d6b1a00b72ef7f8876d0bc6a78a4c9985c53614041512063
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/test-debug) = %{version}
Provides:       crate(%{pkgname}/test-low-transition-point) = %{version}

%description
Source code for takopackized Rust crate "ordermap"

%package     -n %{name}+serde
Summary:        Hash table with consistent order and fast iteration - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-1) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ordermap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde-1" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
