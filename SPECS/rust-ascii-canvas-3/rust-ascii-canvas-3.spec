# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ascii-canvas
%global full_version 3.0.0
%global pkgname ascii-canvas-3

Name:           rust-ascii-canvas-3
Version:        3.0.0
Release:        %autorelease
Summary:        Rust crate "ascii-canvas"
License:        Apache-2.0 OR MIT
URL:            https://github.com/nikomatsakis/ascii-canvas
#!RemoteAsset:  sha256:8824ecca2e851cec16968d54a01dd372ef8f95b244fb84b84e70128be347c3c6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(term-0.7/default) >= 0.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ascii-canvas"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
