# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kernel32-sys
%global full_version 0.2.2
%global pkgname kernel32-sys-0.2

Name:           rust-kernel32-sys-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "kernel32-sys"
License:        MIT
URL:            https://github.com/retep998/winapi-rs
#!RemoteAsset:  sha256:7507624b29483431c0ba2d82aece8ca6cdba9382bff4ddd0f7490560c056098d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winapi-0.2/default) >= 0.2.5
Requires:       crate(winapi-build-0.1) >= 0.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
See winapi for types and constants.
Source code for takopackized Rust crate "kernel32-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
