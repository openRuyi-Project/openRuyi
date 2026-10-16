# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name humansize
%global full_version 2.1.3
%global pkgname humansize-2

Name:           rust-humansize-2
Version:        2.1.3
Release:        %autorelease
Summary:        Rust crate "humansize"
License:        MIT OR Apache-2.0
URL:            https://github.com/LeopoldArkham/humansize
#!RemoteAsset:  sha256:6cb51c9a029ddc91b07a787f1d86b53ccfa49b0e86688c946ebe8d3555685dd7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libm-0.2/default) >= 0.2.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/impl-style) = %{version}
Provides:       crate(%{pkgname}/no-alloc) = %{version}

%description
Source code for takopackized Rust crate "humansize"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
