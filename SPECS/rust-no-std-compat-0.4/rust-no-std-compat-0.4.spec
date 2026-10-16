# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name no-std-compat
%global full_version 0.4.1
%global pkgname no-std-compat-0.4

Name:           rust-no-std-compat-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "no-std-compat"
License:        MIT
URL:            https://gitlab.com/jD91mZM2/no-std-compat
#!RemoteAsset:  sha256:b93853da6d84c2e3c7d730d6473e8817692dd89be387eb01b94d7f108ecb5b8c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/compat-macros) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "no-std-compat"

%package     -n %{name}+hashbrown
Summary:        `#![no_std]` compatibility layer that will make porting your crate to no_std *easy* - feature "hashbrown" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.8/default) >= 0.8.1
Provides:       crate(%{pkgname}/compat-hash) = %{version}
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust no-std-compat crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compat_hash" feature.

%package     -n %{name}+spin
Summary:        `#![no_std]` compatibility layer that will make porting your crate to no_std *easy* - feature "spin" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spin-0.5/default) >= 0.5.2
Provides:       crate(%{pkgname}/compat-sync) = %{version}
Provides:       crate(%{pkgname}/spin) = %{version}

%description -n %{name}+spin
This metapackage enables feature "spin" for the Rust no-std-compat crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compat_sync" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
