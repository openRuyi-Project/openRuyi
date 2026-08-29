# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thousands
%global full_version 0.2.0
%global pkgname thousands-0.2

Name:           rust-thousands-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "thousands"
License:        MIT OR Apache-2.0
URL:            https://github.com/tov/thousands-rs
#!RemoteAsset:  sha256:3bf63baf9f5039dadc247375c29eb13706706cfde997d0330d05aa63a77d8820
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thousands"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
