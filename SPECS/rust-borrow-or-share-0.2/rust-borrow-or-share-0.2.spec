# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name borrow-or-share
%global full_version 0.2.4
%global pkgname borrow-or-share-0.2

Name:           rust-borrow-or-share-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "borrow-or-share"
License:        MIT-0
URL:            https://github.com/yescallop/borrow-or-share
#!RemoteAsset:  sha256:dc0b364ead1874514c8c2855ab558056ebfeb775653e7ae45ff72f28f8f3166c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "borrow-or-share"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
