# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enum-map
%global full_version 2.7.3
%global pkgname enum-map-2

Name:           rust-enum-map-2
Version:        2.7.3
Release:        %autorelease
Summary:        Rust crate "enum-map"
License:        MIT OR Apache-2.0
URL:            https://codeberg.org/xfix/enum-map
#!RemoteAsset:  sha256:6866f3bfdf8207509a033af1a75a7b08abda06bbaaeae6669323fd5a097df2e9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(enum-map-derive-0.17/default) >= 0.17.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "enum-map"

%package     -n %{name}+arbitrary
Summary:        Map with C-like enum keys represented internally as an array - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust enum-map crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Map with C-like enum keys represented internally as an array - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.16
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust enum-map crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
