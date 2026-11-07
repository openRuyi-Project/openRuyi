# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strsim
%global full_version 0.8.0
%global pkgname strsim-0.8

Name:           rust-strsim-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "strsim"
License:        MIT
URL:            https://github.com/dguo/strsim-rs
#!RemoteAsset:  sha256:8ea5119cdb4c55b55d432abb513a0429384878c15dde60cc77b1c99de1a95a6a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Includes Hamming, Levenshtein, OSA, Damerau-Levenshtein, Jaro, and Jaro-Winkler.
Source code for takopackized Rust crate "strsim"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
