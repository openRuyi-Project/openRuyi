# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde-json-fmt
%global full_version 0.1.0
%global pkgname serde-json-fmt-0.1

Name:           rust-serde-json-fmt-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "serde-json-fmt"
License:        MIT
URL:            https://github.com/jwodder/serde-json-fmt
#!RemoteAsset:  sha256:a4a33b7a5f52a26d520099339add40c48baf2e5ada194c8cc1b18cafa2b5e419
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1.0) >= 1.0.219
Requires:       crate(serde-json-1.0/default) >= 1.0.140
Requires:       crate(smartstring-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "serde-json-fmt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
