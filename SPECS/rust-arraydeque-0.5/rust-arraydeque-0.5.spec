# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arraydeque
%global full_version 0.5.1
%global pkgname arraydeque-0.5

Name:           rust-arraydeque-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "arraydeque"
License:        MIT OR Apache-2.0
URL:            https://github.com/andylokandy/arraydeque
#!RemoteAsset:  sha256:7d902e3d592a523def97af8f317b08ce16b7ab854c1985a0c671e6f15cebc236
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "arraydeque"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
