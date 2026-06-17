# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lru-slab
%global full_version 0.1.2
%global pkgname lru-slab-0.1

Name:           rust-lru-slab-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "lru-slab"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/Ralith/lru-slab
#!RemoteAsset:  sha256:112b39cec0b298b6c1999fee3e31427f74f676e4cb9879ed1a121b43661a4154
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lru-slab"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
