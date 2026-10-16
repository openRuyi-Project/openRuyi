# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fixedbitset
%global full_version 0.1.9
%global pkgname fixedbitset-0.1

Name:           rust-fixedbitset-0.1
Version:        0.1.9
Release:        %autorelease
Summary:        Rust crate "fixedbitset"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/fixedbitset
#!RemoteAsset:  sha256:86d4de0081402f5e88cdac65c8dcdcc73118c1a7a465e2a05f0da05843a8ea33
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fixedbitset"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
