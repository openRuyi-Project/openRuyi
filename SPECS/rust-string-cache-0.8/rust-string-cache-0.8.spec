# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name string_cache
%global full_version 0.8.9
%global pkgname string-cache-0.8

Name:           rust-string-cache-0.8
Version:        0.8.9
Release:        %autorelease
Summary:        Rust crate "string_cache"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/string-cache
#!RemoteAsset:  sha256:bf776ba3fa74f83bf4b63c3dcbbf82173db2632ed8452cb2d891d33f459de70f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(new-debug-unreachable-1/default) >= 1.0.2
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(phf-shared-0.11/default) >= 0.11.0
Requires:       crate(precomputed-hash-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "string_cache"

%package     -n %{name}+malloc-size-of
Summary:        String interning library for Rust, developed as part of the Servo project - feature "malloc_size_of"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malloc-size-of-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/malloc-size-of) = %{version}

%description -n %{name}+malloc-size-of
This metapackage enables feature "malloc_size_of" for the Rust string_cache crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        String interning library for Rust, developed as part of the Servo project - feature "serde" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-support) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust string_cache crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "serde_support" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
