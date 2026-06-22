# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name defmt-parser
%global full_version 1.0.0
%global pkgname defmt-parser-1

Name:           rust-defmt-parser-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "defmt-parser"
License:        MIT OR Apache-2.0
URL:            https://github.com/knurling-rs/defmt
#!RemoteAsset:  sha256:10d60334b3b2e7c9d91ef8150abfb6fa4c1c39ebbcf4a81c2e346aad939fee3e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "defmt-parser"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
