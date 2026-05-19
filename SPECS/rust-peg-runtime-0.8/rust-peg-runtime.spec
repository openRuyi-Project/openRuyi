# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name peg-runtime
%global full_version 0.8.5
%global pkgname peg-runtime-0.8

Name:           rust-peg-runtime-0.8
Version:        0.8.5
Release:        %autorelease
Summary:        Rust crate "peg-runtime"
License:        MIT
URL:            https://github.com/kevinmehall/rust-peg
#!RemoteAsset:  sha256:132dca9b868d927b35b5dd728167b2dee150eb1ad686008fc71ccb298b776fca
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable)

%description
To use rust-peg, see the `peg` crate.
Source code for takopackized Rust crate "peg-runtime"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
