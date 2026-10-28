# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thiserror-impl
%global full_version 2.0.20
%global pkgname thiserror-impl-2

Name:           rust-thiserror-impl-2
Version:        2.0.20
Release:        %autorelease
Summary:        Rust crate "thiserror-impl"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/thiserror
#!RemoteAsset:  sha256:bc04cd3e1236dd4a98afca4569f2deb3f120e5422a4023be2cb683f8486292af
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.74
Requires:       crate(quote-1/default) >= 1.0.35
Requires:       crate(syn-3/default) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thiserror-impl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
