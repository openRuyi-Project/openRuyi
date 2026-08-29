# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name matchit
%global full_version 0.8.4
%global pkgname matchit-0.8

Name:           rust-matchit-0.8
Version:        0.8.4
Release:        %autorelease
Summary:        Rust crate "matchit"
License:        MIT AND BSD-3-Clause
URL:            https://github.com/ibraheemdev/matchit
#!RemoteAsset:  sha256:47e1ffaa40ddd1f3ed91f717a33c8c0ee23fff369e3aa8772b9605cc1d22f4c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/test-helpers) = %{version}

%description
Source code for takopackized Rust crate "matchit"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
