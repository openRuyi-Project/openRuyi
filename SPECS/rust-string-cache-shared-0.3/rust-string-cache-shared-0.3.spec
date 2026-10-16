# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name string_cache_shared
%global full_version 0.3.0
%global pkgname string-cache-shared-0.3

Name:           rust-string-cache-shared-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "string_cache_shared"
License:        MIT  OR  Apache-2.0
URL:            https://github.com/servo/string-cache
#!RemoteAsset:  sha256:b1884d1bc09741d466d9b14e6d37ac89d6909cbcac41dd9ae982d4d063bbedfc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "string_cache_shared"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
