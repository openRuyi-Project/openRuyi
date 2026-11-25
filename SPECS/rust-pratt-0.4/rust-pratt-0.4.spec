# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pratt
%global full_version 0.4.0
%global pkgname pratt-0.4

Name:           rust-pratt-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "pratt"
License:        MIT
URL:            https://github.com/segeljakt/pratt/
#!RemoteAsset:  sha256:17e0a4425d076f0718b820673a38fbf3747080c61017eeb0dd79bc7e472b8bb8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pratt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
