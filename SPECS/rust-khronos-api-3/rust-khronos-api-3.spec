# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name khronos_api
%global full_version 3.1.0
%global pkgname khronos-api-3

Name:           rust-khronos-api-3
Version:        3.1.0
Release:        %autorelease
Summary:        Rust crate "khronos_api"
License:        Apache-2.0
URL:            https://github.com/brendanzab/gl-rs/
#!RemoteAsset:  sha256:e2db585e1d738fc771bf08a151420d3ed193d9d895a36df7f6f8a9456b911ddc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "khronos_api"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
