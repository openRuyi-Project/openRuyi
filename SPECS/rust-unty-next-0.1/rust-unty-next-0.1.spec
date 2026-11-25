# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unty-next
%global full_version 0.1.2
%global pkgname unty-next-0.1

Name:           rust-unty-next-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "unty-next"
License:        MIT OR Apache-2.0
URL:            https://github.com/Apich-Organization/unty
#!RemoteAsset:  sha256:16062d030850f35054e37746427b9febb74a2f24c9c6dd6fa2d0c13c5f53221e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unty-next"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
