# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name matchit
%global full_version 0.9.2
%global pkgname matchit-0.9

Name:           rust-matchit-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "matchit"
License:        MIT AND BSD-3-Clause
URL:            https://github.com/ibraheemdev/matchit
#!RemoteAsset:  sha256:8863b587001c1b9a8a4e36008cebc6b3612cb1226fe2de94858e06092687b608
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/test-helpers)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "matchit"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
