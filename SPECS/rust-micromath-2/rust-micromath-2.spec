# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name micromath
%global full_version 2.1.0
%global pkgname micromath-2

Name:           rust-micromath-2
Version:        2.1.0
Release:        %autorelease
Summary:        Rust crate "micromath"
License:        Apache-2.0 OR MIT
URL:            https://github.com/tarcieri/micromath
#!RemoteAsset:  sha256:c3c8dda44ff03a2f238717214da50f65d5a53b45cd213a7370424ffdb6fae815
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/quaternion) = %{version}
Provides:       crate(%{pkgname}/statistics) = %{version}
Provides:       crate(%{pkgname}/vector) = %{version}

%description
Optimizes for performance and small code size at the cost of precision.
Source code for takopackized Rust crate "micromath"

%package     -n %{name}+num-traits
Summary:        Embedded-friendly math library featuring fast floating point approximations (with small code size) for common arithmetic operations, trigonometry, 2D/3D vector types, statistical analysis, and quaternions - feature "num-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/num-traits) = %{version}

%description -n %{name}+num-traits
Optimizes for performance and small code size at the cost of precision.
This metapackage enables feature "num-traits" for the Rust micromath crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
