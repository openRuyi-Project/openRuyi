# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name socket2
%global full_version 0.5.10
%global pkgname socket2-0.5

Name:           rust-socket2-0.5
Version:        0.5.10
Release:        %autorelease
Summary:        Rust crate "socket2"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/socket2
#!RemoteAsset:  sha256:e22376abed350d73dd1cd119b57ffccad95b4e585a7cda43e286245ce23c0678
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.174
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/all)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "socket2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
