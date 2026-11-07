# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name term
%global full_version 0.2.14
%global pkgname term-0.2

Name:           rust-term-0.2
Version:        0.2.14
Release:        %autorelease
Summary:        Rust crate "term"
License:        MIT OR Apache-2.0
URL:            https://github.com/Stebalien/term
#!RemoteAsset:  sha256:f2077e54d38055cf1ca0fd7933a2e00cd3ec8f6fed352b2a377f06dcdaaf3281
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(kernel32-sys-0.2/default) >= 0.2.0
Requires:       crate(winapi-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "term"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
