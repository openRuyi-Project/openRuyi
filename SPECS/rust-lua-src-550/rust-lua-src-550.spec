# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lua-src
%global full_version 550.0.0
%global pkgname lua-src-550

Name:           rust-lua-src-550
Version:        550.0.0
Release:        %autorelease
Summary:        Rust crate "lua-src"
License:        MIT
URL:            https://github.com/mlua-rs/lua-src-rs
#!RemoteAsset:  sha256:e836dc8ae16806c9bdcf42003a88da27d163433e3f9684c52f0301258004a4fb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1/default) >= 1.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/ucid) = %{version}

%description
Source code for takopackized Rust crate "lua-src"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
