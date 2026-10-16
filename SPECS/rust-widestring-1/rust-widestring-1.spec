# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name widestring
%global full_version 1.2.1
%global pkgname widestring-1

Name:           rust-widestring-1
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "widestring"
License:        MIT OR Apache-2.0
URL:            https://github.com/VoidStarKat/widestring-rs
#!RemoteAsset:  sha256:72069c3113ab32ab29e5584db3c6ec55d416895e60715417b5b883a357c3e471
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/debugger-visualizer) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Both `u16` and `u32` string types are provided, including support for UTF-16 and UTF-32, malformed encoding, C-style strings, etc.
Source code for takopackized Rust crate "widestring"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
