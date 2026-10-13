# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name volatile-register
%global full_version 0.2.2
%global pkgname volatile-register-0.2

Name:           rust-volatile-register-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "volatile-register"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/volatile-register
#!RemoteAsset:  sha256:de437e2a6208b014ab52972a27e59b33fa2920d3e00fe05026167a1c509d19cc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(vcell-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "volatile-register"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
