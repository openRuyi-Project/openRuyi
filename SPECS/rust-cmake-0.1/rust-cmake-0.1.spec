# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cmake
%global full_version 0.1.58
%global pkgname cmake-0.1

Name:           rust-cmake-0.1
Version:        0.1.58
Release:        %autorelease
Summary:        Rust crate "cmake"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cmake-rs
#!RemoteAsset:  sha256:c0f78a02292a74a88ac736019ab962ece0bc380e3f977bf72e376c5d78ff0678
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1/default) >= 1.2.46

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cmake"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
