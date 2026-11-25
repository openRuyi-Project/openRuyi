# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pagable_derive
%global full_version 0.4.2
%global pkgname pagable-derive-0.4

Name:           rust-pagable-derive-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "pagable_derive"
License:        Apache-2.0
URL:            FIXME
#!RemoteAsset:  sha256:7332d8709796f21d6ffd1b0565e2846717cb56700f3cc1b1a3d0ba242c0b1512
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pagable_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
