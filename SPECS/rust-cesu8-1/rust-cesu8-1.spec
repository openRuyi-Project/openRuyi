# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cesu8
%global full_version 1.1.0
%global pkgname cesu8-1

Name:           rust-cesu8-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "cesu8"
License:        Apache-2.0 OR MIT
URL:            https://github.com/emk/cesu8-rs
#!RemoteAsset:  sha256:6d43a04d8753f35258c91f8ec639f792891f748a1edbd759cf1dcea3382ad83c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "cesu8"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
