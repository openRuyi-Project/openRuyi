# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name headers-core
%global full_version 0.3.0
%global pkgname headers-core-0.3

Name:           rust-headers-core-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "headers-core"
License:        MIT
URL:            https://hyper.rs
#!RemoteAsset:  sha256:54b4a22553d4242c49fddb9ba998a99962b5cc6f22cb5a3482bec22522403ce4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(http-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "headers-core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
