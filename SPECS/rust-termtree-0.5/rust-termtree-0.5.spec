# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name termtree
%global full_version 0.5.1
%global pkgname termtree-0.5

Name:           rust-termtree-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "termtree"
License:        MIT
URL:            https://github.com/rust-cli/termtree
#!RemoteAsset:  sha256:8f50febec83f5ee1df3015341d8bd429f2d1cc62bcba7ea2076759d315084683
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "termtree"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
