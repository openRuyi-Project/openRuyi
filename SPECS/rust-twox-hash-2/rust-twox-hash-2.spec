# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name twox-hash
%global full_version 2.1.2
%global pkgname twox-hash-2

Name:           rust-twox-hash-2
Version:        2.1.2
Release:        %autorelease
Summary:        Rust crate "twox-hash"
License:        MIT
URL:            https://github.com/shepmaster/twox-hash
#!RemoteAsset:  sha256:9ea3136b675547379c4bd395ca6b938e5ad3c3d20fad76e7fe85f9e0d011419c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/xxhash3-128) = %{version}
Provides:       crate(%{pkgname}/xxhash3-64) = %{version}
Provides:       crate(%{pkgname}/xxhash32) = %{version}
Provides:       crate(%{pkgname}/xxhash64) = %{version}

%description
Source code for takopackized Rust crate "twox-hash"

%package     -n %{name}+default
Summary:        The XXHash and XXH3 algorithms - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/random) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/xxhash3-128) = %{version}
Requires:       crate(%{pkgname}/xxhash3-64) = %{version}
Requires:       crate(%{pkgname}/xxhash32) = %{version}
Requires:       crate(%{pkgname}/xxhash64) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust twox-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+random
Summary:        The XXHash and XXH3 algorithms - feature "random"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.9/thread-rng) >= 0.9.0
Provides:       crate(%{pkgname}/random) = %{version}

%description -n %{name}+random
This metapackage enables feature "random" for the Rust twox-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialize
Summary:        The XXHash and XXH3 algorithms - feature "serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serialize
This metapackage enables feature "serialize" for the Rust twox-hash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
