# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name alloc-no-stdlib
%global full_version 2.0.4
%global pkgname alloc-no-stdlib-2

Name:           rust-alloc-no-stdlib-2
Version:        2.0.4
Release:        %autorelease
Summary:        Rust crate "alloc-no-stdlib"
License:        BSD-3-Clause
URL:            https://github.com/dropbox/rust-alloc-no-stdlib
#!RemoteAsset:  sha256:cc7bb162ec39d46ab1ca8c77bf72e890535becd1751bb45f64c597edb4c8c6b3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unsafe) = %{version}

%description
This allows a package with nostd to allocate memory dynamically and be used either with a custom allocator, items on the stack, or by a package that wishes to simply use Box<>. It also provides options to use calloc or a mutable global variable for pre-zeroed memory
Source code for takopackized Rust crate "alloc-no-stdlib"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
