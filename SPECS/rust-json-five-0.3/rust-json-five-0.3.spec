# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name json-five
%global full_version 0.3.1
%global pkgname json-five-0.3

Name:           rust-json-five-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "json-five"
License:        MIT
URL:            https://github.com/spyoungtech/json-five-rs
#!RemoteAsset:  sha256:865f2d01a4549c1fd8c60640c03ae5249eb374cd8cde8b905628d4b1af95c87c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-general-category-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unlimited-depth) = %{version}

%description
Source code for takopackized Rust crate "json-five"

%package     -n %{name}+serde
Summary:        JSON5 parser with round-trip capabilities and compatible with the serde data model - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust json-five crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
