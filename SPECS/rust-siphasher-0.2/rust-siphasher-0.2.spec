# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name siphasher
%global full_version 0.2.3
%global pkgname siphasher-0.2

Name:           rust-siphasher-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "siphasher"
License:        MIT OR Apache-2.0
URL:            https://docs.rs/siphasher
#!RemoteAsset:  sha256:0b8de496cf83d4ed58b6be86c3a275b8602f6ffe98d3024a869e124147a9a3ac
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "siphasher"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
