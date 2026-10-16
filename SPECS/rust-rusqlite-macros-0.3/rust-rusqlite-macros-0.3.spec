# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rusqlite-macros
%global full_version 0.3.0
%global pkgname rusqlite-macros-0.3

Name:           rust-rusqlite-macros-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "rusqlite-macros"
License:        MIT
URL:            https://github.com/rusqlite/rusqlite
#!RemoteAsset:  sha256:ecdc5e5d64f172916dfc8a0b0f7876de19b899e7a5f1d5b2c04c722cc78e0e45
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fallible-iterator-0.3/default) >= 0.3.0
Requires:       crate(litrs-0.4) >= 0.4.0
Requires:       crate(sqlite3-parser-0.13/yynoerrorrecovery) >= 0.13.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rusqlite-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
