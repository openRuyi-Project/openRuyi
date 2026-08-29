# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytemuck_derive
%global full_version 1.10.2
%global pkgname bytemuck-derive-1

Name:           rust-bytemuck-derive-1
Version:        1.10.2
Release:        %autorelease
Summary:        Rust crate "bytemuck_derive"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/bytemuck
#!RemoteAsset:  sha256:f9abbd1bc6865053c427f7198e6af43bfdedc55ab791faed4fbd361d789575ff
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.60
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bytemuck_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
