# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name once_cell_polyfill
%global full_version 1.70.2
%global pkgname once-cell-polyfill-1.0

Name:           rust-once-cell-polyfill-1.0
Version:        1.70.2
Release:        %autorelease
Summary:        Rust crate "once_cell_polyfill"
License:        MIT OR Apache-2.0
URL:            https://github.com/polyfill-rs/once_cell_polyfill
#!RemoteAsset:  sha256:384b8ab6d37215f3c5301a95a4accb5d64aa607f1fcb26a11b5303878451b4fe
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "once_cell_polyfill"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
