# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ufmt-write
%global full_version 0.1.0
%global pkgname ufmt-write-0.1

Name:           rust-ufmt-write-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "ufmt-write"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/ufmt
#!RemoteAsset:  sha256:e87a2ed6b42ec5e28cc3b94c09982969e9227600b2e3dcbc1db927a84c06bd69
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for the Rust crate "ufmt-write"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
