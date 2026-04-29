# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name indoc
%global full_version 2.0.5
%global pkgname indoc-2.0

Name:           rust-indoc-2.0
Version:        2.0.5
Release:        %autorelease
Summary:        Rust crate "indoc"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/indoc
#!RemoteAsset:  sha256:b248f5224d1d606005e02c97f5aa4e88eeb230488bcc03bc9ca4d7991399f2b5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(indoc) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "indoc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
