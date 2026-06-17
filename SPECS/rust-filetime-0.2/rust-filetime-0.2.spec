# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name filetime
%global full_version 0.2.27
%global pkgname filetime-0.2

Name:           rust-filetime-0.2
Version:        0.2.27
Release:        %autorelease
Summary:        Rust crate "filetime"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/filetime
#!RemoteAsset:  sha256:f98844151eee8917efc50bd9e8318cb963ae8b297431495d3f758616ea5c57db
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.27
Requires:       crate(libredox-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "filetime"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
