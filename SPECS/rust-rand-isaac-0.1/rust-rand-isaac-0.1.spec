# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_isaac
%global full_version 0.1.1
%global pkgname rand-isaac-0.1

Name:           rust-rand-isaac-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "rand_isaac"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_isaac
#!RemoteAsset:  sha256:ded997c9d5f13925be2a6fd7e66bf1872597f759fd9dd93513dd7e92e5a5ee08
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.3) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rand_isaac"

%package     -n %{name}+serde
Summary:        ISAAC random number generator - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand_isaac crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        ISAAC random number generator - feature "serde1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Requires:       crate(rand-core-0.3/serde1) >= 0.3.0
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust rand_isaac crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        ISAAC random number generator - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.38
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust rand_isaac crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
