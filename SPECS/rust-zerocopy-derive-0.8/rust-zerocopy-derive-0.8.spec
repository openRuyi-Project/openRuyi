# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy-derive
%global full_version 0.8.50
%global pkgname zerocopy-derive-0.8

Name:           rust-zerocopy-derive-0.8
Version:        0.8.50
Release:        %autorelease
Summary:        Rust crate "zerocopy-derive"
License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://github.com/google/zerocopy
#!RemoteAsset:  sha256:0b631b19d36a892ab55420c92dbc83ccd79274f25be714855d3074aa71cab639
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.1
Requires:       crate(quote-1/default) >= 1.0.40
Requires:       crate(syn-2/default) >= 2.0.46
Requires:       crate(syn-2/full) >= 2.0.46
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zerocopy-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
