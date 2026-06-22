# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name postcard-derive
%global full_version 0.2.2
%global pkgname postcard-derive-0.2

Name:           rust-postcard-derive-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "postcard-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/jamesmunns/postcard
#!RemoteAsset:  sha256:e0232bd009a197ceec9cc881ba46f727fcd8060a2d8d6a9dde7a69030a6fe2bb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "postcard-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
