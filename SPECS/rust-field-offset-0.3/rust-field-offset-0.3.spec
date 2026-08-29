# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name field-offset
%global full_version 0.3.6
%global pkgname field-offset-0.3

Name:           rust-field-offset-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "field-offset"
License:        MIT OR Apache-2.0
URL:            https://github.com/Diggsey/rust-field-offset
#!RemoteAsset:  sha256:38e2275cc4e4fc009b0669731a1e5ab7ebf11f469eaede2bab9309a5b4d6057f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memoffset-0.9/default) >= 0.9.0
Requires:       crate(rustc-version-0.4) >= 0.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "field-offset"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
