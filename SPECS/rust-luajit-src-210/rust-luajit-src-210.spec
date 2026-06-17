# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name luajit-src
%global full_version 210.6.6+707c12b
%global pkgname luajit-src-210

Name:           rust-luajit-src-210
Version:        210.6.6
Release:        %autorelease
Summary:        Rust crate "luajit-src"
License:        MIT
URL:            https://github.com/mlua-rs/luajit-src-rs
#!RemoteAsset:  sha256:a86cc925d4053d0526ae7f5bc765dbd0d7a5d1a63d43974f4966cb349ca63295
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1/default) >= 1.2.0
Requires:       crate(which-8/default) >= 8.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "luajit-src"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
