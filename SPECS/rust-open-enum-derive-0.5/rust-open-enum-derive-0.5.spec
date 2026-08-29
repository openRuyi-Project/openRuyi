# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name open-enum-derive
%global full_version 0.5.2
%global pkgname open-enum-derive-0.5

Name:           rust-open-enum-derive-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "open-enum-derive"
License:        Apache-2.0
URL:            https://github.com/kupiakos/open-enum/tree/main/derive
#!RemoteAsset:  sha256:8d1296fab5231654a5aec8bf9e87ba4e3938c502fc4c3c0425a00084c78944be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.43
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/repr-c) = %{version}

%description
Source code for takopackized Rust crate "open-enum-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
