# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name blake2b_simd
%global full_version 1.0.5
%global pkgname blake2b-simd-1

Name:           rust-blake2b-simd-1
Version:        1.0.5
Release:        %autorelease
Summary:        Rust crate "blake2b_simd"
License:        MIT
URL:            https://github.com/oconnor663/blake2_simd
#!RemoteAsset:  sha256:3560a7b1951efe814fcd721938313adc56753ca39f4b23847d7e9a2402f5dbff
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7) >= 0.7.0
Requires:       crate(constant-time-eq-0.4) >= 0.4.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/uninline-portable) = %{version}

%description
Source code for takopackized Rust crate "blake2b_simd"

%package     -n %{name}+std
Summary:        Pure Rust BLAKE2b implementation with dynamic SIMD - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(constant-time-eq-0.4/std) >= 0.4.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust blake2b_simd crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
