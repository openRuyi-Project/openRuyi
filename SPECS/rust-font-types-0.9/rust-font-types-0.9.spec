# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name font-types
%global full_version 0.9.0
%global pkgname font-types-0.9

Name:           rust-font-types-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "font-types"
License:        MIT OR Apache-2.0
URL:            https://github.com/googlefonts/fontations
#!RemoteAsset:  sha256:02a596f5713680923a2080d86de50fe472fb290693cf0f701187a1c8b36996b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "font-types"

%package     -n %{name}+bytemuck
Summary:        Scalar types used in fonts - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.13.1
Requires:       crate(bytemuck-1/derive) >= 1.13.1
Requires:       crate(bytemuck-1/min-const-generics) >= 1.13.1
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust font-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Scalar types used in fonts - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust font-types crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
