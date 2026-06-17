# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-linebreak
%global full_version 0.1.5
%global pkgname unicode-linebreak-0.1

Name:           rust-unicode-linebreak-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "unicode-linebreak"
License:        Apache-2.0
URL:            https://github.com/axelf4/unicode-linebreak
#!RemoteAsset:  sha256:3b09c83c3c29d37506a3e260c08c03743a6bb66a9cd432c6934ab501a190571f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unicode-linebreak"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
