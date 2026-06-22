# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ndk-context
%global full_version 0.1.1
%global pkgname ndk-context-0.1

Name:           rust-ndk-context-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "ndk-context"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-windowing/android-ndk-rs
#!RemoteAsset:  sha256:27b02d87554356db9e9a873add8782d4ea6e3e58ea071a9adb9a2e8ddb884a8b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ndk-context"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
