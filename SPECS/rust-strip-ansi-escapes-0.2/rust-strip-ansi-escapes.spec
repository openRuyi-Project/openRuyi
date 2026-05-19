# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strip-ansi-escapes
%global full_version 0.2.1
%global pkgname strip-ansi-escapes-0.2

Name:           rust-strip-ansi-escapes-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "strip-ansi-escapes"
License:        Apache-2.0/MIT
URL:            https://github.com/luser/strip-ansi-escapes
#!RemoteAsset:  sha256:2a8f8038e7e7969abb3f1b7c2a811225e9296da208539e0f79c5251d6cac0025
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(vte-0.14) >= 0.14.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "strip-ansi-escapes"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
