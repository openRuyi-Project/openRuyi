# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name base64
%global full_version 0.13.1
%global pkgname base64-0.13

Name:           rust-base64-0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Rust crate "base64"
License:        MIT OR Apache-2.0
URL:            https://github.com/marshallpierce/rust-base64
#!RemoteAsset:  sha256:9e1b586273c5702936fe7b7d6896644d8be71e6314cfe09d3167c95f712589e8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "base64"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
