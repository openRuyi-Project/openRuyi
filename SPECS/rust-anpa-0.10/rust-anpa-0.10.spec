# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anpa
%global full_version 0.10.0
%global pkgname anpa-0.10

Name:           rust-anpa-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "anpa"
License:        MIT OR Apache-2.0
URL:            https://github.com/habbbe/anpa-rs
#!RemoteAsset:  sha256:4d032745fe46100dbcb28ee6e30f12c4b148786f8889e07cd0a3445eeb54970f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/semver) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "anpa"

%package     -n %{name}+build-bench
Summary:        Generic monadic parser combinator library inspired by Haskell's parsec - feature "build_bench"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/json) = %{version}
Requires:       crate(%{pkgname}/semver) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/build-bench) = %{version}

%description -n %{name}+build-bench
This metapackage enables feature "build_bench" for the Rust anpa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
