# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pretty_assertions
%global full_version 1.4.1
%global pkgname pretty-assertions-1.0

Name:           rust-pretty-assertions-1.0
Version:        1.4.1
Release:        %autorelease
Summary:        Rust crate "pretty_assertions"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-pretty-assertions/rust-pretty-assertions
#!RemoteAsset:  sha256:3ae130e2f271fbc2ac3a40fb1d07180839cdbbe443c7a27e1e3c13c5cac0116d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(diff-0.1/default) >= 0.1.13
Requires:       crate(yansi-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "pretty_assertions"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
