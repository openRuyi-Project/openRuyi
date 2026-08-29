# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lzxd
%global full_version 0.2.6
%global pkgname lzxd-0.2

Name:           rust-lzxd-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "lzxd"
License:        MIT OR Apache-2.0
URL:            https://github.com/Lonami/lzxd
#!RemoteAsset:  sha256:7b29dffab797218e12e4df08ef5d15ab9efca2504038b1b32b9b32fc844b39c9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lzxd"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
