# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name plain
%global full_version 0.2.3
%global pkgname plain-0.2

Name:           rust-plain-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "plain"
License:        MIT OR Apache-2.0
URL:            https://github.com/randomites/plain
#!RemoteAsset:  sha256:b4596b6d070b27117e987119b4dac604f3c58cfb0b191112e24771b2faeac1a6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "plain"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
