# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitmaps
%global full_version 2.1.0
%global pkgname bitmaps-2

Name:           rust-bitmaps-2
Version:        2.1.0
Release:        %autorelease
Summary:        Rust crate "bitmaps"
License:        MPL-2.0+
URL:            https://github.com/bodil/bitmaps
#!RemoteAsset:  sha256:031043d04099746d8db04daf1fa424b2bc8bd69d92b25962dcde24da39ab64a2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(typenum-1/default) >= 1.10.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "bitmaps"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
