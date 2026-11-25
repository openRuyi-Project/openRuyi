# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_starlark
%global full_version 0.1.19
%global pkgname serde-starlark-0.1

Name:           rust-serde-starlark-0.1
Version:        0.1.19
Release:        %autorelease
Summary:        Rust crate "serde_starlark"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/serde-starlark
#!RemoteAsset:  sha256:73193c7bfc91575d7df89b2a0d8f3522c6c39efbad6b991aaa1ed5377bf209cf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1/alloc) >= 1.0.220

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_starlark"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
