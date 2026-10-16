# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lru-cache
%global full_version 0.1.2
%global pkgname lru-cache-0.1

Name:           rust-lru-cache-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "lru-cache"
License:        MIT OR Apache-2.0
URL:            https://github.com/contain-rs/lru-cache
#!RemoteAsset:  sha256:31e24f1ad8321ca0e8a1e0ac13f23cb668e6f5466c2c57319f6a5cf1cc8e3b1c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(linked-hash-map-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lru-cache"

%package     -n %{name}+heapsize
Summary:        Cache that holds a limited number of key-value pairs - feature "heapsize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heapsize-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/heapsize) = %{version}

%description -n %{name}+heapsize
This metapackage enables feature "heapsize" for the Rust lru-cache crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heapsize-impl
Summary:        Cache that holds a limited number of key-value pairs - feature "heapsize_impl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/heapsize) = %{version}
Requires:       crate(linked-hash-map-0.5/heapsize-impl) >= 0.5.0
Provides:       crate(%{pkgname}/heapsize-impl) = %{version}

%description -n %{name}+heapsize-impl
This metapackage enables feature "heapsize_impl" for the Rust lru-cache crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
