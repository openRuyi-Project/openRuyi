# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name deflate64
%global full_version 0.1.10
%global pkgname deflate64-0.1

Name:           rust-deflate64-0.1
Version:        0.1.10
Release:        %autorelease
Summary:        Rust crate "deflate64"
License:        MIT
URL:            https://github.com/anatawa12/deflate64-rs#readme
#!RemoteAsset:  sha256:26bf8fc351c5ed29b5c2f0cbbac1b209b74f60ecd62e675a998df72c49af5204
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "deflate64"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
