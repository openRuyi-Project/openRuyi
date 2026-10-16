# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_pcg
%global full_version 0.1.2
%global pkgname rand-pcg-0.1

Name:           rust-rand-pcg-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "rand_pcg"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_pcg
#!RemoteAsset:  sha256:abf9b09b01790cfe0364f52bf32995ea3c39f4d2dd011eac241d2914146d0b44
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-0.1) >= 0.1.0
Requires:       crate(rand-core-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rand_pcg"

%package     -n %{name}+serde
Summary:        Selected PCG random number generators - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand_pcg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        Selected PCG random number generators - feature "serde1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust rand_pcg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Selected PCG random number generators - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.38
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust rand_pcg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
