# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name peg-macros
%global full_version 0.8.5
%global pkgname peg-macros-0.8

Name:           rust-peg-macros-0.8
Version:        0.8.5
Release:        %autorelease
Summary:        Rust crate "peg-macros"
License:        MIT
URL:            https://github.com/kevinmehall/rust-peg
#!RemoteAsset:  sha256:6298ab04c202fa5b5d52ba03269fb7b74550b150323038878fe6c372d8280f71
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(peg-runtime-0.8/default) >= 0.8.5
Requires:       crate(proc-macro2-1/default) >= 1.0.24
Requires:       crate(quote-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/trace) = %{version}

%description
To use rust-peg, see the `peg` crate.
Source code for takopackized Rust crate "peg-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
