# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lab
%global full_version 0.11.0
%global pkgname lab-0.11

Name:           rust-lab-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "lab"
License:        MIT
URL:            https://github.com/TooManyBees/lab
#!RemoteAsset:  sha256:bf36173d4167ed999940f804952e6b08197cae5ad5d572eb4db150ce8ad5d58f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lab"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
