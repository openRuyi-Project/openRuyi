# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name associative-cache
%global full_version 2.0.0
%global pkgname associative-cache-2

Name:           rust-associative-cache-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "associative-cache"
License:        MIT OR Apache-2.0
URL:            https://github.com/fitzgen/associative-cache
#!RemoteAsset:  sha256:b993cd767a2bc7307dd87622311ca22c44329cc7a21366206bfa0896827b2bad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "associative-cache"

%package     -n %{name}+rand
Summary:        Generic N-way associative cache with fixed-size capacity and random or least recently used (LRU) replacement - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8/default) >= 0.8.5
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust associative-cache crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
