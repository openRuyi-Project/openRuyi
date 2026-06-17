# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ref-cast
%global full_version 1.0.25
%global pkgname ref-cast-1

Name:           rust-ref-cast-1
Version:        1.0.25
Release:        %autorelease
Summary:        Rust crate "ref-cast"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/ref-cast
#!RemoteAsset:  sha256:f354300ae66f76f1c85c5f84693f0ce81d747e2c3f21a45fef496d89c960bf7d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ref-cast-impl-1/default) >= 1.0.25
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ref-cast"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
