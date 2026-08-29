# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hash32
%global full_version 0.2.1
%global pkgname hash32-0.2

Name:           rust-hash32-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "hash32"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/hash32
#!RemoteAsset:  sha256:b0c35f58762feb77d74ebe43bdbc3210f09be9fe6742234d573bacc26ed92b67
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1) >= 1.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hash32"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
