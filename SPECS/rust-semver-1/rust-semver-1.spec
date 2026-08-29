# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name semver
%global full_version 1.0.28
%global pkgname semver-1

Name:           rust-semver-1
Version:        1.0.28
Release:        %autorelease
Summary:        Rust crate "semver"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/semver
#!RemoteAsset:  sha256:8a7852d02fc848982e0c167ef163aaff9cd91dc640ba85e263cb1ce46fae51cd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "semver"

%package     -n %{name}+serde
Summary:        Parser and evaluator for Cargo's flavor of Semantic Versioning - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1) >= 1.0.220
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust semver crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
