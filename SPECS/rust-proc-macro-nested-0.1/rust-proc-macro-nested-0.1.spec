# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-nested
%global full_version 0.1.7
%global pkgname proc-macro-nested-0.1

Name:           rust-proc-macro-nested-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "proc-macro-nested"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/proc-macro-hack
#!RemoteAsset:  sha256:bc881b2c22681370c6a780e47af9840ef841837bc98118431d4e1868bd0c1086
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-nested"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
