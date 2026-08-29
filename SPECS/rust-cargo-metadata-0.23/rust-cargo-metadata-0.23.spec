# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo_metadata
%global full_version 0.23.1
%global pkgname cargo-metadata-0.23

Name:           rust-cargo-metadata-0.23
Version:        0.23.1
Release:        %autorelease
Summary:        Rust crate "cargo_metadata"
License:        MIT
URL:            https://github.com/oli-obk/cargo_metadata
#!RemoteAsset:  sha256:ef987d17b0a113becdd19d3d0022d04d7ef41f9efe4f3fb63ac44ba61df3ade9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(camino-1/default) >= 1.1.10
Requires:       crate(camino-1/serde1) >= 1.1.10
Requires:       crate(cargo-platform-0.3/default) >= 0.3.0
Requires:       crate(semver-1/default) >= 1.0.26
Requires:       crate(semver-1/serde) >= 1.0.26
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(serde-json-1/default) >= 1.0.142
Requires:       crate(serde-json-1/unbounded-depth) >= 1.0.142
Requires:       crate(thiserror-2/default) >= 2.0.12
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "cargo_metadata"

%package     -n %{name}+derive-builder
Summary:        Structured access to the output of `cargo metadata` - feature "derive_builder" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/builder) = %{version}
Provides:       crate(%{pkgname}/derive-builder) = %{version}

%description -n %{name}+derive-builder
This metapackage enables feature "derive_builder" for the Rust cargo_metadata crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "builder" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
