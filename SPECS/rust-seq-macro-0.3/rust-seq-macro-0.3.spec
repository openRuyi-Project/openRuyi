# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name seq-macro
%global full_version 0.3.6
%global pkgname seq-macro-0.3

Name:           rust-seq-macro-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "seq-macro"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/seq-macro
#!RemoteAsset:  sha256:1bc711410fbe7399f390ca1c3b60ad0f53f80e95c5eb935e52268a0e2cd49acc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "seq-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
