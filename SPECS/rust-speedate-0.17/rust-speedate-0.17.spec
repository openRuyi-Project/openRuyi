# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name speedate
%global full_version 0.17.0
%global pkgname speedate-0.17

Name:           rust-speedate-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "speedate"
License:        MIT
URL:            https://github.com/pydantic/speedate/
#!RemoteAsset:  sha256:aba069c070b5e213f2a094deb7e5ed50ecb092be36102a4f4042e8d2056d060e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lexical-parse-float-1/default) >= 1.0.5
Requires:       crate(strum-0.27/default) >= 0.27.0
Requires:       crate(strum-0.27/derive) >= 0.27.0
Requires:       crate(strum-macros-0.27/default) >= 0.27.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "speedate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
