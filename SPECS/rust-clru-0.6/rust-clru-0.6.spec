# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clru
%global full_version 0.6.3
%global pkgname clru-0.6

Name:           rust-clru-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "clru"
License:        MIT
URL:            https://github.com/marmeladema/clru-rs
#!RemoteAsset:  sha256:197fd99cb113a8d5d9b6376f3aa817f32c1078f2343b714fff7d2ca44fdf67d5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clru"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
