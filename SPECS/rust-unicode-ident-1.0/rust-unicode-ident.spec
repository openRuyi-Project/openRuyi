# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-ident
%global full_version 1.0.24
%global pkgname unicode-ident-1.0

Name:           rust-unicode-ident-1.0
Version:        1.0.24
Release:        %autorelease
Summary:        Rust crate "unicode-ident"
License:        (MIT OR Apache-2.0) AND Unicode-3.0
URL:            https://github.com/dtolnay/unicode-ident
#!RemoteAsset:  sha256:e6e4313cd5fcd3dad5cafa179702e2b244f760991f45397d14d4ebf38247da75
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "unicode-ident"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
