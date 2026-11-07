# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name semver
%global full_version 0.9.0
%global pkgname semver-0.9

Name:           rust-semver-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "semver"
License:        MIT OR Apache-2.0
URL:            https://docs.rs/crate/semver/
#!RemoteAsset:  sha256:1d7eb9ef2c18661902cc47e535f9bc51b78acd254da71d375c2f6720d9a40403
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(semver-parser-0.7/default) >= 0.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "semver"

%package     -n %{name}+serde
Summary:        Semantic version parsing and comparison - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/ci) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust semver crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ci" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
