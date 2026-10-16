# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrayvec
%global full_version 0.5.2
%global pkgname arrayvec-0.5

Name:           rust-arrayvec-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "arrayvec"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/arrayvec
#!RemoteAsset:  sha256:23b62fc65de8e4e7f52534fb52b0f3ed04746ae267519eef2a83941e8085068b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/array-sizes-129-255) = %{version}
Provides:       crate(%{pkgname}/array-sizes-33-128) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-const-fn) = %{version}

%description
Implements fixed capacity ArrayVec and ArrayString.
Source code for takopackized Rust crate "arrayvec"

%package     -n %{name}+serde
Summary:        Vector with fixed capacity, backed by an array (it can be stored on the stack too) - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Implements fixed capacity ArrayVec and ArrayString.
This metapackage enables feature "serde" for the Rust arrayvec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
