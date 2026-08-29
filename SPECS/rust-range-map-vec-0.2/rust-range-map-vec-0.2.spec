# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name range_map_vec
%global full_version 0.2.0
%global pkgname range-map-vec-0.2

Name:           rust-range-map-vec-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "range_map_vec"
License:        MIT
URL:            https://github.com/microsoft/range_map_vec
#!RemoteAsset:  sha256:7cc2191ec1fd850e3ede4cf09ccfd40a33df561111f73e96e1b7c3f9eee31328
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "range_map_vec"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
