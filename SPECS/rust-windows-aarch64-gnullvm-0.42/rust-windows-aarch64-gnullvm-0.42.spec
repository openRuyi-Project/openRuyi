# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows_aarch64_gnullvm
%global full_version 0.42.2
%global pkgname windows-aarch64-gnullvm-0.42

Name:           rust-windows-aarch64-gnullvm-0.42
Version:        0.42.2
Release:        %autorelease
Summary:        Rust crate "windows_aarch64_gnullvm"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:597a5118570b68bc08d8d59125332c54f1ba9d9adeedeef5b99b02ba2b0698f8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "windows_aarch64_gnullvm"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
