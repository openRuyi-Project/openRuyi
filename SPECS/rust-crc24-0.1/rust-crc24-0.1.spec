# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crc24
%global full_version 0.1.6
%global pkgname crc24-0.1

Name:           rust-crc24-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "crc24"
License:        MIT OR Apache-2.0
URL:            https://github.com/sellibitze/crc24-rs
#!RemoteAsset:  sha256:fd121741cf3eb82c08dd3023eb55bf2665e5f60ec20f89760cf836ae4562e6a0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "crc24"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
