# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy-derive
%global full_version 0.7.35
%global pkgname zerocopy-derive-0.7

Name:           rust-zerocopy-derive-0.7
Version:        0.7.35
Release:        %autorelease
Summary:        Rust crate "zerocopy-derive"
License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://github.com/google/zerocopy
#!RemoteAsset:  sha256:fa4f8080344d4671fb4e831a13ad1e68092748387dfc4f55e356242fae12ce3e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.1
Requires:       crate(quote-1/default) >= 1.0.10
Requires:       crate(syn-2/default) >= 2.0.31

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zerocopy-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
