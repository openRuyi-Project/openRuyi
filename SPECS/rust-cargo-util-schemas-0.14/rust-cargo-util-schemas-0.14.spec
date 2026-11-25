# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-util-schemas
%global full_version 0.14.2
%global pkgname cargo-util-schemas-0.14

Name:           rust-cargo-util-schemas-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "cargo-util-schemas"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:46262ca4393669799a8df4852e81672ddea46657e73294b1a846f0d5c71509ed
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(jiff-0.2/serde) >= 0.2.23
Requires:       crate(jiff-0.2/std) >= 0.2.23
Requires:       crate(semver-1/default) >= 1.0.27
Requires:       crate(semver-1/serde) >= 1.0.27
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-untagged-0.1/default) >= 0.1.9
Requires:       crate(serde-value-0.7/default) >= 0.7.0
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(toml-1/serde) >= 1.1.2
Requires:       crate(unicode-ident-1/default) >= 1.0.24
Requires:       crate(url-2/default) >= 2.5.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo-util-schemas"

%package     -n %{name}+unstable-schema
Summary:        Deserialization schemas for Cargo - feature "unstable-schema"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-1/default) >= 1.2.1
Requires:       crate(schemars-1/preserve-order) >= 1.2.1
Requires:       crate(schemars-1/semver1) >= 1.2.1
Requires:       crate(serde-json-1/default) >= 1.0.149
Provides:       crate(%{pkgname}/unstable-schema) = %{version}

%description -n %{name}+unstable-schema
This metapackage enables feature "unstable-schema" for the Rust cargo-util-schemas crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
