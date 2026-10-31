# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pkg-config
%global full_version 0.3.34
%global pkgname pkg-config-0.3

Name:           rust-pkg-config-0.3
Version:        0.3.34
Release:        %autorelease
Summary:        Rust crate "pkg-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/pkg-config-rs
#!RemoteAsset:  sha256:f6b464fbc74e149a392436b17d523f769e057cb6877f6a5c4618bc6f11800548
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pkg-config"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
