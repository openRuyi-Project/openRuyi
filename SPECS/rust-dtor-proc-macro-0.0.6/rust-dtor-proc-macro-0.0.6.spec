# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dtor-proc-macro
%global full_version 0.0.6
%global pkgname dtor-proc-macro-0.0.6

Name:           rust-dtor-proc-macro-0.0.6
Version:        0.0.6
Release:        %autorelease
Summary:        Rust crate "dtor-proc-macro"
License:        Apache-2.0 OR MIT
URL:            https://github.com/mmastrac/rust-ctor
#!RemoteAsset:  sha256:f678cf4a922c215c63e0de95eb1ff08a958a81d47e485cf9da1e27bf6305cfa5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dtor-proc-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
