# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name better_default
%global full_version 1.0.5
%global pkgname better-default-1

Name:           rust-better-default-1
Version:        1.0.5
Release:        %autorelease
Summary:        Rust crate "better_default"
License:        Apache-2.0
URL:            https://github.com/NovaliX-Dev/better_default
#!RemoteAsset:  sha256:7b9a5040dce49a7642c97ccb1ae59567098967b5d52c29773f1299a42d23bb39
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.79
Requires:       crate(quote-1/default) >= 1.0.36
Requires:       crate(syn-2/default) >= 2.0.58
Requires:       crate(syn-2/full) >= 2.0.58

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "better_default"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
