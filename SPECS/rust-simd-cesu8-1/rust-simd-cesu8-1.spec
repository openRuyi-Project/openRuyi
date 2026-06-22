# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name simd_cesu8
%global full_version 1.1.1
%global pkgname simd-cesu8-1

Name:           rust-simd-cesu8-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "simd_cesu8"
License:        Apache-2.0 OR MIT
URL:            https://github.com/seancroach/simd_cesu8
#!RemoteAsset:  sha256:94f90157bb87cddf702797c5dadfa0be7d266cdf49e22da2fcaa32eff75b2c33
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustc-version-0.4) >= 0.4.0
Requires:       crate(simdutf8-0.1) >= 0.1.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "simd_cesu8"

%package     -n %{name}+std
Summary:        Extremely fast, SIMD accelerated, encoding and decoding library for CESU-8 and Modified UTF-8 - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simdutf8-0.1/std) >= 0.1.4
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust simd_cesu8 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
