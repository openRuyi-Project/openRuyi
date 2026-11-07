# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cexpr
%global full_version 0.3.6
%global pkgname cexpr-0.3

Name:           rust-cexpr-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "cexpr"
License:        Apache-2.0 OR MIT
URL:            https://github.com/jethrogb/rust-cexpr
#!RemoteAsset:  sha256:fce5b5fb86b0c57c20c834c1b412fd09c77c8a59b9473f86272709e78874cd1d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nom-4/default) >= 4.0.0
Requires:       crate(nom-4/verbose-errors) >= 4.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cexpr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
