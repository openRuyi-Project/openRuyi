# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitflags
%global full_version 2.13.0
%global pkgname bitflags-2

Name:           rust-bitflags-2
Version:        2.13.0
Release:        %autorelease
Summary:        Rust crate "bitflags"
License:        MIT OR Apache-2.0
URL:            https://github.com/bitflags/bitflags
#!RemoteAsset:  sha256:b4388bee8683e3d04af747c73422af53102d2bd24d9eadb6cbc100baef4b43f8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/example-generated) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "bitflags"

%package     -n %{name}+arbitrary
Summary:        Macro to generate structures which behave like bitflags - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Macro to generate structures which behave like bitflags - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.12.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-core
Summary:        Macro to generate structures which behave like bitflags - feature "serde_core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.228
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-core) = %{version}

%description -n %{name}+serde-core
This metapackage enables feature "serde_core" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
