# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-id
%global full_version 0.3.6
%global pkgname unicode-id-0.3

Name:           rust-unicode-id-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "unicode-id"
License:        MIT OR Apache-2.0
URL:            https://github.com/Boshen/unicode-id
#!RemoteAsset:  sha256:70ba288e709927c043cbe476718d37be306be53fb1fafecd0dbe36d072be2580
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/bench)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/no-std)

%description
Source code for takopackized Rust crate "unicode-id"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
