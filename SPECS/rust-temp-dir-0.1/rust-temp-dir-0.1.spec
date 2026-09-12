# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name temp-dir
%global full_version 0.1.16
%global pkgname temp-dir-0.1

Name:           rust-temp-dir-0.1
Version:        0.1.16
Release:        %autorelease
Summary:        Rust crate "temp-dir"
License:        Apache-2.0
URL:            https://gitlab.com/leonhard-llc/ops
#!RemoteAsset:  sha256:83176759e9416cf81ee66cb6508dbfe9c96f20b8b56265a39917551c23c70964
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "temp-dir"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
