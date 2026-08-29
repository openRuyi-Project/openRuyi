# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unit-prefix
%global full_version 0.5.2
%global pkgname unit-prefix-0.5

Name:           rust-unit-prefix-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "unit-prefix"
License:        MIT
URL:            https://codeberg.org/commons-rs/unit-prefix
#!RemoteAsset:  sha256:81e544489bf3d8ef66c953931f56617f423cd4b5494be343d9b9d3dda037b9a3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "unit-prefix"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
