# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name comma
%global full_version 1.0.0
%global pkgname comma-1

Name:           rust-comma-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "comma"
License:        MIT
URL:            https://github.com/emctague/comma
#!RemoteAsset:  sha256:55b672471b4e9f9e95499ea597ff64941a309b2cdbffcc46f2cc5e2d971fd335
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "comma"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
