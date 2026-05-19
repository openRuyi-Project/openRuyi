# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name natord
%global full_version 1.0.9
%global pkgname natord-1.0

Name:           rust-natord-1.0
Version:        1.0.9
Release:        %autorelease
Summary:        Rust crate "natord"
License:        MIT
URL:            https://github.com/lifthrasiir/rust-natord
#!RemoteAsset:  sha256:308d96db8debc727c3fd9744aac51751243420e46edf401010908da7f8d5e57c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "natord"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
