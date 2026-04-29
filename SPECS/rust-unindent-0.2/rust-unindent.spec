# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unindent
%global full_version 0.2.3
%global pkgname unindent-0.2

Name:           rust-unindent-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "unindent"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/indoc
#!RemoteAsset:  sha256:c7de7d73e1754487cb58364ee906a499937a0dfabd86bcb980fa99ec8c8fa2ce
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(unindent) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "unindent"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
