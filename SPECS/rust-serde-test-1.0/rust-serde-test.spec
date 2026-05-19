# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_test
%global full_version 1.0.177
%global pkgname serde-test-1.0

Name:           rust-serde-test-1.0
Version:        1.0.177
Release:        %autorelease
Summary:        Rust crate "serde_test"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/test
#!RemoteAsset:  sha256:7f901ee573cab6b3060453d2d5f0bae4e6d628c23c0a962ff9b5f1d7c8d4f1ed
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1.0/default) >= 1.0.228
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "serde_test"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
