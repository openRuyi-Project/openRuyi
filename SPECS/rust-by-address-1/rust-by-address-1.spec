# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name by_address
%global full_version 1.2.1
%global pkgname by-address-1

Name:           rust-by-address-1
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "by_address"
License:        MIT OR Apache-2.0
URL:            https://github.com/mbrubeck/by_address
#!RemoteAsset:  sha256:64fa3c856b712db6612c019f14756e64e4bcea13337a6b33b696333a9eaa2d06
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "by_address"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
