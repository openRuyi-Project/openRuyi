# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memoffset
%global full_version 0.6.5
%global pkgname memoffset-0.6

Name:           rust-memoffset-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "memoffset"
License:        MIT
URL:            https://github.com/Gilnaa/memoffset
#!RemoteAsset:  sha256:5aa361d4faea93603064a027415f07bd8e1d5c88c9fbf68bf56a285428fd79ce
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable-const) = %{version}

%description
Source code for takopackized Rust crate "memoffset"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
