# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name is_terminal_polyfill
%global full_version 1.70.2
%global pkgname is-terminal-polyfill-1

Name:           rust-is-terminal-polyfill-1
Version:        1.70.2
Release:        %autorelease
Summary:        Rust crate "is_terminal_polyfill"
License:        MIT OR Apache-2.0
URL:            https://github.com/polyfill-rs/is_terminal_polyfill
#!RemoteAsset:  sha256:a6cb138bb79a146c1bd460005623e142ef0181e3d0219cb493e02f7d08a35695
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "is_terminal_polyfill"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
