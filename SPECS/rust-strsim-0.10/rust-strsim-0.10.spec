# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strsim
%global full_version 0.10.0
%global pkgname strsim-0.10

Name:           rust-strsim-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "strsim"
License:        MIT
URL:            https://github.com/dguo/strsim-rs
#!RemoteAsset:  sha256:73473c0e59e6d5812c5dfe2a064a6444949f089e20eec9a2e5506596494e4623
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Includes Hamming, Levenshtein, OSA, Damerau-Levenshtein, Jaro, Jaro-Winkler, and Sørensen-Dice.
Source code for takopackized Rust crate "strsim"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
