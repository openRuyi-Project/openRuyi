# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unscanny
%global full_version 0.1.0
%global pkgname unscanny-0.1

Name:           rust-unscanny-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "unscanny"
License:        MIT OR Apache-2.0
URL:            https://github.com/typst/unscanny
#!RemoteAsset:  sha256:e9df2af067a7953e9c3831320f35c1cc0600c30d44d9f7a12b01db1cd88d6b47
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unscanny"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
