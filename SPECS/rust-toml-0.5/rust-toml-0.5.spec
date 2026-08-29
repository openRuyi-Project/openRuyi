# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml
%global full_version 0.5.2
%global pkgname toml-0.5

Name:           rust-toml-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "toml"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/toml-rs
#!RemoteAsset:  sha256:a54ae44b0b2c443e7ef6dd3be16a776bae4daa40684f81e15126bc04e7747308
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.97
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
Source code for takopackized Rust crate "toml"

%package     -n %{name}+linked-hash-map
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "linked-hash-map" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linked-hash-map-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/linked-hash-map) = %{version}
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+linked-hash-map
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "linked-hash-map" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "preserve_order" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
