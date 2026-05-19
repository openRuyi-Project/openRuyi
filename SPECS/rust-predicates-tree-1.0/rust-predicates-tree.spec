# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name predicates-tree
%global full_version 1.0.12
%global pkgname predicates-tree-1.0

Name:           rust-predicates-tree-1.0
Version:        1.0.12
Release:        %autorelease
Summary:        Rust crate "predicates-tree"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/predicates-rs/tree/master/crates/tree
#!RemoteAsset:  sha256:72dd2d6d381dfb73a193c7fca536518d7caee39fc8503f74e7dc0be0531b425c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(predicates-core-1.0/default) >= 1.0.9
Requires:       crate(termtree-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "predicates-tree"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
