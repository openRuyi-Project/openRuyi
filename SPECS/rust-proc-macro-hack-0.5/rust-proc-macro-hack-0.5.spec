# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-hack
%global full_version 0.5.20+deprecated
%global pkgname proc-macro-hack-0.5

Name:           rust-proc-macro-hack-0.5
Version:        0.5.20
Release:        %autorelease
Summary:        Rust crate "proc-macro-hack"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/proc-macro-hack
#!RemoteAsset:  sha256:dc375e1527247fe1a97d8b7156678dfe7c1af2fc075c9a4db3690ecd2a148068
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-hack"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
