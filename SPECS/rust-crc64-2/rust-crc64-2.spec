# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crc64
%global full_version 2.0.0
%global pkgname crc64-2

Name:           rust-crc64-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "crc64"
License:        BSD-3-Clause
URL:            https://github.com/badboy/crc64-rs
#!RemoteAsset:  sha256:2707e3afba5e19b75d582d88bc79237418f2a2a2d673d01cf9b03633b46e98f3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "crc64"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
