# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name svgtypes
%global full_version 0.15.3
%global pkgname svgtypes-0.15

Name:           rust-svgtypes-0.15
Version:        0.15.3
Release:        %autorelease
Summary:        Rust crate "svgtypes"
License:        Apache-2.0 OR MIT
URL:            https://github.com/linebender/svgtypes
#!RemoteAsset:  sha256:68c7541fff44b35860c1a7a47a7cadf3e4a304c457b58f9870d9706ece028afc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(kurbo-0.11/default) >= 0.11.0
Requires:       crate(siphasher-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "svgtypes"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
