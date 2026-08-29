# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name foreign-types-macros
%global full_version 0.2.3
%global pkgname foreign-types-macros-0.2

Name:           rust-foreign-types-macros-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "foreign-types-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/sfackler/foreign-types
#!RemoteAsset:  sha256:1a5c6c585bc94aaf2c7b51dd4c2ba22680844aba4c687be581871a6f518c5742
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "foreign-types-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
