# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex-syntax
%global full_version 0.3.9
%global pkgname regex-syntax-0.3

Name:           rust-regex-syntax-0.3
Version:        0.3.9
Release:        %autorelease
Summary:        Rust crate "regex-syntax"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex
#!RemoteAsset:  sha256:f9ec002c35e86791825ed294b50008eea9ddfc8def4420124fbc6b08db834957
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "regex-syntax"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
