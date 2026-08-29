# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name outref
%global full_version 0.5.2
%global pkgname outref-0.5

Name:           rust-outref-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "outref"
License:        MIT
URL:            https://github.com/Nugine/outref
#!RemoteAsset:  sha256:1a80800c0488c3a21695ea981a54918fbb37abf04f4d0720c453632255e2ff0e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "outref"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
