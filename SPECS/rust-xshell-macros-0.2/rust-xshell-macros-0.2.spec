# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xshell-macros
%global full_version 0.2.7
%global pkgname xshell-macros-0.2

Name:           rust-xshell-macros-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "xshell-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/matklad/xshell
#!RemoteAsset:  sha256:32ac00cd3f8ec9c1d33fb3e7958a82df6989c42d747bd326c822b1d625283547
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "xshell-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
