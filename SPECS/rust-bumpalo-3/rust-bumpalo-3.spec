# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bumpalo
%global full_version 3.20.2
%global pkgname bumpalo-3

Name:           rust-bumpalo-3
Version:        3.20.2
Release:        %autorelease
Summary:        Rust crate "bumpalo"
License:        MIT OR Apache-2.0
URL:            https://github.com/fitzgen/bumpalo
#!RemoteAsset:  sha256:5d20789868f4b01b2f2caec9f5c4e0213b41e3e5702a50157d699ae31ced2fcb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/allocator-api) = %{version}
Provides:       crate(%{pkgname}/bench-allocator-api) = %{version}
Provides:       crate(%{pkgname}/boxed) = %{version}
Provides:       crate(%{pkgname}/collections) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "bumpalo"

%package     -n %{name}+allocator-api2
Summary:        Fast bump allocation arena for Rust - feature "allocator-api2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(allocator-api2-0.2) >= 0.2.8
Provides:       crate(%{pkgname}/allocator-api2) = %{version}

%description -n %{name}+allocator-api2
This metapackage enables feature "allocator-api2" for the Rust bumpalo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fast bump allocation arena for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.171
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bumpalo crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
