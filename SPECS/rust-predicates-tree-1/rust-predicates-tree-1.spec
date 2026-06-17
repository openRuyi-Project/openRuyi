# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name predicates-tree
%global full_version 1.0.13
%global pkgname predicates-tree-1

Name:           rust-predicates-tree-1
Version:        1.0.13
Release:        %autorelease
Summary:        Rust crate "predicates-tree"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/predicates-rs
#!RemoteAsset:  sha256:d0de1b847b39c8131db0467e9df1ff60e6d0562ab8e9a16e568ad0fdb372e2f2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(predicates-core-1/default) >= 1.0.0
Requires:       crate(termtree-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "predicates-tree"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
