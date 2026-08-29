# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name platforms
%global full_version 4.1.0
%global pkgname platforms-4

Name:           rust-platforms-4
Version:        4.1.0
Release:        %autorelease
Summary:        Rust crate "platforms"
License:        Apache-2.0 OR MIT
URL:            https://rustsec.org
#!RemoteAsset:  sha256:acff5dfd42135d89cd7ad74a8c52813bbec91bf62c018ddd89390127767caab5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "platforms"

%package     -n %{name}+serde
Summary:        Rust platform registry with information about valid Rust platforms (target triple, target_arch, target_os) sourced from the Rust compiler - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust platforms crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
