# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo_toml
%global full_version 1.0.0
%global pkgname cargo-toml-1

Name:           rust-cargo-toml-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "cargo_toml"
License:        Apache-2.0 OR MIT
URL:            https://gitlab.com/lib.rs/cargo_toml
#!RemoteAsset:  sha256:aa61aec073ec94791433ddf3df2323ff9d1711557c2a0eefb0f99cb4f8dca520
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(semver-1/serde) >= 1.0.26
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(toml-1/default) >= 1.0.1
Provides:       crate(%{pkgname}) = %{version}

%description
Cargo.toml struct definitions for parsing with Serde.
Source code for takopackized Rust crate "cargo_toml"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
