# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name path-tree
%global full_version 0.8.3
%global pkgname path-tree-0.8

Name:           rust-path-tree-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "path-tree"
License:        MIT OR Apache-2.0
URL:            https://github.com/viz-rs/path-tree
#!RemoteAsset:  sha256:c2a97453bc21a968f722df730bfe11bd08745cb50d1300b0df2bda131dece136
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(smallvec-1/const-new) >= 1.14.0
Requires:       crate(smallvec-1/default) >= 1.14.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "path-tree"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
