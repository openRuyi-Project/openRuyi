# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ascii-canvas
%global full_version 2.0.0
%global pkgname ascii-canvas-2

Name:           rust-ascii-canvas-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "ascii-canvas"
License:        Apache-2.0 OR MIT
URL:            https://github.com/nikomatsakis/ascii-canvas
#!RemoteAsset:  sha256:ff8eb72df928aafb99fe5d37b383f2fe25bd2a765e3e5f7c365916b6f2463a29
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(term-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ascii-canvas"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
