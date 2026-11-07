# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml
%global full_version 0.4.10
%global pkgname toml-0.4

Name:           rust-toml-0.4
Version:        0.4.10
Release:        %autorelease
Summary:        Rust crate "toml"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/toml-rs
#!RemoteAsset:  sha256:758664fc71a3a69038656bee8b6be6477d2a6c315a6b81f7081f591bffa4111f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
Source code for takopackized Rust crate "toml"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
