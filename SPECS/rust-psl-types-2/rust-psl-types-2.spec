# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name psl-types
%global full_version 2.0.11
%global pkgname psl-types-2

Name:           rust-psl-types-2
Version:        2.0.11
Release:        %autorelease
Summary:        Rust crate "psl-types"
License:        MIT OR Apache-2.0
URL:            https://github.com/addr-rs/psl-types
#!RemoteAsset:  sha256:33cb294fe86a74cbcf50d4445b37da762029549ebeea341421c7c70370f86cac
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "psl-types"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
