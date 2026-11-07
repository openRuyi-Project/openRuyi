# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syntex_syntax
%global full_version 0.8.0
%global pkgname syntex-syntax-0.8

Name:           rust-syntex-syntax-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "syntex_syntax"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-syntex
#!RemoteAsset:  sha256:0d8cf37db56bbe93d0133fc7d60ea3ba5a0dde4219d39100081e2971fdadb103
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-0.3/default) >= 0.3.2
Requires:       crate(libc-0.1/default) >= 0.1.8
Requires:       crate(log-0.3/default) >= 0.3.1
Requires:       crate(rustc-serialize-0.3/default) >= 0.3.15
Requires:       crate(term-0.2/default) >= 0.2.10
Requires:       crate(unicode-xid-0.0.2/default) >= 0.0.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Patch2000:      2000-Use-compatible-versioned-dependencies.patch

%description
Source code for takopackized Rust crate "syntex_syntax"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
