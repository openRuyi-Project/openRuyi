# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqlite3-parser
%global full_version 0.13.0
%global pkgname sqlite3-parser-0.13

Name:           rust-sqlite3-parser-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "sqlite3-parser"
License:        Apache-2.0 OR MIT
URL:            https://github.com/gwenn/lemon-rs
#!RemoteAsset:  sha256:eb5307dad6cb84730ce8bdefde56ff4cf95fe516972d52e2bbdc8a8cd8f2520b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(fallible-iterator-0.3/default) >= 0.3.0
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(memchr-2/default) >= 2.0.0
Requires:       crate(phf-0.11/default) >= 0.11.0
Requires:       crate(phf-0.11/uncased) >= 0.11.0
Requires:       crate(phf-codegen-0.11) >= 0.11.0
Requires:       crate(phf-shared-0.11) >= 0.11.0
Requires:       crate(phf-shared-0.11/uncased) >= 0.11.0
Requires:       crate(uncased-0.9) >= 0.9.0
Requires:       crate(uncased-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/ndebug) = %{version}
Provides:       crate(%{pkgname}/yycoverage) = %{version}
Provides:       crate(%{pkgname}/yynoerrorrecovery) = %{version}
Provides:       crate(%{pkgname}/yytrackmaxstackdepth) = %{version}

%description
Source code for takopackized Rust crate "sqlite3-parser"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
