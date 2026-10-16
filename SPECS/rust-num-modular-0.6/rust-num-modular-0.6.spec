# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-modular
%global full_version 0.6.5
%global pkgname num-modular-0.6

Name:           rust-num-modular-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "num-modular"
License:        Apache-2.0
URL:            https://github.com/cmpute/num-modular
#!RemoteAsset:  sha256:bd8e500409e6cd603b03e477c26a6caecdc27ac58979a53e881c75eafc079f44
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Supports various backends including num-bigint, etc..
Source code for takopackized Rust crate "num-modular"

%package     -n %{name}+num-bigint
Summary:        Efficient integer division and modular arithmetic operations with generic number types - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4) >= 0.4.3
Requires:       crate(num-integer-0.1) >= 0.1.44
Requires:       crate(num-traits-0.2) >= 0.2.14
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
Supports various backends including num-bigint, etc..
This metapackage enables feature "num-bigint" for the Rust num-modular crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-traits
Summary:        Efficient integer division and modular arithmetic operations with generic number types - feature "num-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2) >= 0.2.14
Provides:       crate(%{pkgname}/num-traits) = %{version}

%description -n %{name}+num-traits
Supports various backends including num-bigint, etc..
This metapackage enables feature "num-traits" for the Rust num-modular crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
