# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name levenshtein
%global full_version 1.0.5
%global pkgname levenshtein-1

Name:           rust-levenshtein-1
Version:        1.0.5
Release:        %autorelease
Summary:        Rust crate "levenshtein"
License:        MIT
URL:            https://github.com/wooorm/levenshtein-rs
#!RemoteAsset:  sha256:db13adb97ab515a3691f56e4dbab09283d0b86cb45abd991d8634a9d6f501760
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "levenshtein"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
