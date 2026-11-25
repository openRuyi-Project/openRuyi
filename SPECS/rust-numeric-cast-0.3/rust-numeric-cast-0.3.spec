# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name numeric_cast
%global full_version 0.3.0
%global pkgname numeric-cast-0.3

Name:           rust-numeric-cast-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "numeric_cast"
License:        MIT
URL:            https://github.com/Nugine/numeric_cast
#!RemoteAsset:  sha256:a3c00a0c9600379bd32f8972de90676a7672cba3bf4886986bc05902afc1e093
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "numeric_cast"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
