# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name predicates-core
%global full_version 1.0.9
%global pkgname predicates-core-1.0

Name:           rust-predicates-core-1.0
Version:        1.0.9
Release:        %autorelease
Summary:        Rust crate "predicates-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/predicates-rs/tree/master/crates/core
#!RemoteAsset:  sha256:727e462b119fe9c93fd0eb1429a5f7647394014cf3c04ab2c0350eeb09095ffa
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "predicates-core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
