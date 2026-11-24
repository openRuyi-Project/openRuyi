# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name path-dedot
%global full_version 4.0.1
%global pkgname path-dedot-4

Name:           rust-path-dedot-4
Version:        4.0.1
Release:        %autorelease
Summary:        Rust crate "path-dedot"
License:        MIT
URL:            https://magiclen.org/path-dedot
#!RemoteAsset:  sha256:03351d0f1c066c114015408dc6a3e101f080fc03ef9d8d799aa58ec760cac5a6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fixed-workdir) = %{version}

%description
Source code for takopackized Rust crate "path-dedot"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
