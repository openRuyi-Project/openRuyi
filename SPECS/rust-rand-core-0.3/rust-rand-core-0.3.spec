# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_core
%global full_version 0.3.2
%global pkgname rand-core-0.3

Name:           rust-rand-core-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "rand_core"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_core
#!RemoteAsset:  sha256:96f815e01bbd9678b50d927f79aa1cf3ffdfdb1b9787317c1284dadb894ad0e8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rand_core"

%package     -n %{name}+alloc
Summary:        Core random number generator traits and tools for implementation - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rand_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        Core random number generator traits and tools for implementation - feature "serde1"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust rand_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Core random number generator traits and tools for implementation - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand_core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
