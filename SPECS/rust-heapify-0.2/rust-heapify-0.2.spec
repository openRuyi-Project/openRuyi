# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name heapify
%global full_version 0.2.0
%global pkgname heapify-0.2

Name:           rust-heapify-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "heapify"
License:        MIT OR Apache-2.0
URL:            https://github.com/ethereal-sheep/heapify
#!RemoteAsset:  sha256:0049b265b7f201ca9ab25475b22b47fe444060126a51abe00f77d986fc5cc52e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "heapify"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
