# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glob
%global full_version 0.2.11
%global pkgname glob-0.2

Name:           rust-glob-0.2
Version:        0.2.11
Release:        %autorelease
Summary:        Rust crate "glob"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/glob
#!RemoteAsset:  sha256:8be18de09a56b60ed0edf84bc9df007e30040691af7acd1c41874faac5895bfb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "glob"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
