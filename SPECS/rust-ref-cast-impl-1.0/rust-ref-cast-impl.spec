# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ref-cast-impl
%global full_version 1.0.25
%global pkgname ref-cast-impl-1.0

Name:           rust-ref-cast-impl-1.0
Version:        1.0.25
Release:        %autorelease
Summary:        Rust crate "ref-cast-impl"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/ref-cast
#!RemoteAsset:  sha256:b7186006dcb21920990093f30e3dea63b7d6e977bf1256be20c3563a5db070da
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "ref-cast-impl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
