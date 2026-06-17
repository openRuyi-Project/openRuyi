# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pastey
%global full_version 0.1.1
%global pkgname pastey-0.1

Name:           rust-pastey-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "pastey"
License:        MIT OR Apache-2.0
URL:            https://github.com/as1100k/pastey
#!RemoteAsset:  sha256:35fb2e5f958ec131621fdd531e9fc186ed768cbe395337403ae56c17a74c68ec
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Successor of paste.
Source code for takopackized Rust crate "pastey"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
