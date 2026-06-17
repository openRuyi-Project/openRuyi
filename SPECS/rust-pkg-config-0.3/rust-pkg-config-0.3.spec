# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pkg-config
%global full_version 0.3.33
%global pkgname pkg-config-0.3

Name:           rust-pkg-config-0.3
Version:        0.3.33
Release:        %autorelease
Summary:        Rust crate "pkg-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/pkg-config-rs
#!RemoteAsset:  sha256:19f132c84eca552bf34cab8ec81f1c1dcc229b811638f9d283dceabe58c5569e
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
