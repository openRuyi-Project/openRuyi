# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name json5
%global full_version 0.4.1
%global pkgname json5-0.4

Name:           rust-json5-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "json5"
License:        ISC
URL:            https://github.com/callum-oakley/json5-rs
#!RemoteAsset:  sha256:96b0db21af676c1ce64250b5f40f3ce2cf27e4e47cb91ed91eb6fe9350b430c1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pest-2/default) >= 2.0.0
Requires:       crate(pest-derive-2/default) >= 2.0.0
Requires:       crate(serde-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "json5"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
