# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-macros
%global full_version 0.7.1
%global pkgname ratatui-macros-0.7

Name:           rust-ratatui-macros-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "ratatui-macros"
License:        MIT
URL:            https://github.com/ratatui/ratatui
#!RemoteAsset:  sha256:80fac59720679490d89d200df411faa249be728681adcabed3d047ae72c48f1d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ratatui-core-0.1/default) >= 0.1.1
Requires:       crate(ratatui-widgets-0.3) >= 0.3.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ratatui-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
