# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name base64
%global full_version 0.23.1
%global pkgname base64-0.23

Name:           rust-base64-0.23
Version:        0.23.1
Release:        %autorelease
Summary:        Rust crate "base64"
License:        MIT OR Apache-2.0
URL:            https://github.com/marshallpierce/rust-base64
#!RemoteAsset:  sha256:ac07cdecf99051d9a5238b80f35af32cdeba5b336e55d957b318b50137e18da5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/simd-unsafe) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "base64"

%package     -n %{name}+default
Summary:        Encodes and decodes base64 as bytes or utf8 - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/simd-unsafe) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust base64 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
