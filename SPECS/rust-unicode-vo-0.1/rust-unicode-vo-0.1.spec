# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-vo
%global full_version 0.1.0
%global pkgname unicode-vo-0.1

Name:           rust-unicode-vo-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "unicode-vo"
License:        MIT OR Apache-2.0
URL:            https://github.com/RazrFalcon/unicode-vo
#!RemoteAsset:  sha256:b1d386ff53b415b7fe27b50bb44679e2cc4660272694b7b6f3326d8480823a94
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unicode-vo"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
