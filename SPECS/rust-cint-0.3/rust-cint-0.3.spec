# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cint
%global full_version 0.3.1
%global pkgname cint-0.3

Name:           rust-cint-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "cint"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/termhn/cint
#!RemoteAsset:  sha256:7a0e87cdf78571d9fbeff16861c37a006cd718d2433dc6d5b80beaae367d899a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cint"

%package     -n %{name}+bytemuck
Summary:        Lean, minimal, and stable set of types for color interoperation between crates in Rust - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.9.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust cint crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
