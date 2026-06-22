# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asn1
%global full_version 0.24.1
%global pkgname asn1-0.24

Name:           rust-asn1-0.24
Version:        0.24.1
Release:        %autorelease
Summary:        Rust crate "asn1"
License:        BSD-3-Clause
URL:            https://github.com/alex/rust-asn1
#!RemoteAsset:  sha256:c9795210620c0cb3f9a7ce4f882808c38e1ef7b347c90591dceae0886e031fb1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(asn1-derive-0.24/default) >= 0.24.1
Requires:       crate(itoa-1/default) >= 1.0.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "asn1"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
