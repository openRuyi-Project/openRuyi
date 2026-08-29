# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name as-slice
%global full_version 0.2.1
%global pkgname as-slice-0.2

Name:           rust-as-slice-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "as-slice"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/as-slice
#!RemoteAsset:  sha256:516b6b4f0e40d50dcda9365d53964ec74560ad4284da2e7fc97122cd83174516
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(stable-deref-trait-1) >= 1.1.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "as-slice"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
