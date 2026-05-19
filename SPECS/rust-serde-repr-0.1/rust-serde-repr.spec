# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_repr
%global full_version 0.1.20
%global pkgname serde-repr-0.1

Name:           rust-serde-repr-0.1
Version:        0.1.20
Release:        %autorelease
Summary:        Rust crate "serde_repr"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/serde-repr
#!RemoteAsset:  sha256:175ee3e80ae9982737ca543e96133087cbd9a485eecc3bc4de9c1a37b47ea59c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "serde_repr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
