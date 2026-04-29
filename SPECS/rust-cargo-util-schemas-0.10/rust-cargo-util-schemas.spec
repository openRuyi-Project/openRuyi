# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-util-schemas
%global full_version 0.10.2
%global pkgname cargo-util-schemas-0.10

Name:           rust-cargo-util-schemas-0.10
Version:        0.10.2
Release:        %autorelease
Summary:        Rust crate "cargo-util-schemas"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:f714efe9b56ea4bed06b499396e77b68db663a55b16dc3f144d5a5a0dc19788c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(semver-1.0/default) >= 1.0.27
Requires:       crate(semver-1.0/serde) >= 1.0.27
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-untagged-0.1/default) >= 0.1.9
Requires:       crate(serde-value-0.7/default) >= 0.7.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(toml-0.9/serde) >= 0.9.12
Requires:       crate(unicode-xid-0.2/default) >= 0.2.6
Requires:       crate(url-2.0/default) >= 2.5.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cargo-util-schemas"

%package     -n %{name}+unstable-schema
Summary:        Deserialization schemas for Cargo - feature "unstable-schema"
Requires:       crate(%{pkgname})
Requires:       crate(schemars-1.0/default) >= 1.0.4
Requires:       crate(schemars-1.0/preserve-order) >= 1.0.4
Requires:       crate(schemars-1.0/semver1) >= 1.0.4
Requires:       crate(serde-json-1.0/default) >= 1.0.145
Provides:       crate(%{pkgname}/unstable-schema)

%description -n %{name}+unstable-schema
This metapackage enables feature "unstable-schema" for the Rust cargo-util-schemas crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
