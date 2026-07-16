# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytecheck_derive
%global full_version 0.6.12
%global pkgname bytecheck-derive-0.6

Name:           rust-bytecheck-derive-0.6
Version:        0.6.12
Release:        %autorelease
Summary:        Rust crate "bytecheck_derive"
License:        MIT
URL:            https://github.com/djkoloski/bytecheck
#!RemoteAsset:  sha256:3db406d29fbcd95542e92559bed4d8ad92636d1ca8b3b72ede10b4bcc010e659
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "bytecheck_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
