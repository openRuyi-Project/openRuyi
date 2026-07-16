# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lru
%global full_version 0.16.3
%global pkgname lru-0.16

Name:           rust-lru-0.16
Version:        0.16.3
Release:        %autorelease
Summary:        Rust crate "lru"
License:        MIT
URL:            https://github.com/jeromefroe/lru-rs
#!RemoteAsset:  sha256:a1dc47f592c06f33f8e3aea9591776ec7c9f9e4124778ff8a3c3b87159f7e593
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
Requires:       crate(hashbrown-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust lru crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+nightly
Summary:        LRU cache implementation - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hashbrown) = %{version}
Requires:       crate(hashbrown-0.16/nightly) >= 0.16.0
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust lru crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
