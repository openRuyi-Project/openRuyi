# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo_metadata
%global full_version 0.15.4
%global pkgname cargo-metadata-0.15

Name:           rust-cargo-metadata-0.15
Version:        0.15.4
Release:        %autorelease
Summary:        Rust crate "cargo_metadata"
License:        MIT
URL:            https://github.com/oli-obk/cargo_metadata
#!RemoteAsset:  sha256:eee4243f1f26fc7a42710e7439c149e2b10b05472f88090acce52632f231a73a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(camino-1/default) >= 1.0.7
Requires:       crate(camino-1/serde1) >= 1.0.7
Requires:       crate(cargo-platform-0.1/default) >= 0.1.2
Requires:       crate(semver-1/default) >= 1.0.7
Requires:       crate(semver-1/serde) >= 1.0.7
Requires:       crate(serde-1/default) >= 1.0.136
Requires:       crate(serde-1/derive) >= 1.0.136
Requires:       crate(serde-json-1/default) >= 1.0.79
Requires:       crate(serde-json-1/unbounded-depth) >= 1.0.79
Requires:       crate(thiserror-1/default) >= 1.0.31

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo_metadata"

%package     -n %{name}+derive-builder
Summary:        Structured access to the output of `cargo metadata` - feature "derive_builder" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-0.11/default) >= 0.11.1
Provides:       crate(%{pkgname}/builder) = %{version}
Provides:       crate(%{pkgname}/derive-builder) = %{version}

%description -n %{name}+derive-builder
This metapackage enables feature "derive_builder" for the Rust cargo_metadata crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "builder" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
