# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-order
%global full_version 1.2.0
%global pkgname num-order-1

Name:           rust-num-order-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "num-order"
License:        Apache-2.0
URL:            https://github.com/cmpute/num-order
#!RemoteAsset:  sha256:537b596b97c40fcf8056d153049eb22f481c17ebce72a513ec9286e4986d1bb6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-modular-0.6/default) >= 0.6.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "num-order"

%package     -n %{name}+num-bigint
Summary:        Numerically consistent `Eq`, `Ord` and `Hash` implementations for various `num` types (`u32`, `f64`, `num_bigint::BigInt`, etc.) - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-traits) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust num-order crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-complex
Summary:        Numerically consistent `Eq`, `Ord` and `Hash` implementations for various `num` types (`u32`, `f64`, `num_bigint::BigInt`, etc.) - feature "num-complex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-complex-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/num-complex) = %{version}

%description -n %{name}+num-complex
This metapackage enables feature "num-complex" for the Rust num-order crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-rational
Summary:        Numerically consistent `Eq`, `Ord` and `Hash` implementations for various `num` types (`u32`, `f64`, `num_bigint::BigInt`, etc.) - feature "num-rational"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-traits) = %{version}
Requires:       crate(num-rational-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/num-rational) = %{version}

%description -n %{name}+num-rational
This metapackage enables feature "num-rational" for the Rust num-order crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-traits
Summary:        Numerically consistent `Eq`, `Ord` and `Hash` implementations for various `num` types (`u32`, `f64`, `num_bigint::BigInt`, etc.) - feature "num-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/num-traits) = %{version}

%description -n %{name}+num-traits
This metapackage enables feature "num-traits" for the Rust num-order crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
