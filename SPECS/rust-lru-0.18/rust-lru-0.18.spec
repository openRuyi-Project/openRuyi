# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lru
%global full_version 0.18.0
%global pkgname lru-0.18

Name:           rust-lru-0.18
Version:        0.18.0
Release:        %autorelease
Summary:        Rust crate "lru"
License:        MIT
URL:            https://github.com/jeromefroe/lru-rs
#!RemoteAsset:  sha256:8a860605968fce16869fd239cf4237a82f3ac470723415db603b0e8b6c8d4fb9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "lru"

%package     -n %{name}+hashbrown
Summary:        LRU cache implementation - feature "hashbrown" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust lru crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+nightly
Summary:        LRU cache implementation - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hashbrown) = %{version}
Requires:       crate(hashbrown-0.17/nightly) >= 0.17.0
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust lru crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
