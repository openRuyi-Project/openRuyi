# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_lex
%global full_version 0.7.5
%global pkgname clap-lex-0.7

Name:           rust-clap-lex-0.7
Version:        0.7.5
Release:        %autorelease
Summary:        Rust crate "clap_lex"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:b94f61472cee1439c0b966b47e3aca9ae07e45d070759512cd390ea2bebc6675
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "clap_lex"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
