# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_core
%global full_version 0.4.3
%global pkgname rand-core-0.4

Name:           rust-rand-core-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "rand_core"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_core
#!RemoteAsset:  sha256:0e5937858e6fd18cd595d558f90bb5de3b72ae23f9e3763af0e805949b04ef60
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "rand_core"

%package     -n %{name}+serde
Summary:        Core random number generator traits and tools for implementation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        Core random number generator traits and tools for implementation - feature "serde1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust rand_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Core random number generator traits and tools for implementation - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.38
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust rand_core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
