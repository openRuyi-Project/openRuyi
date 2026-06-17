# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yoke-derive
%global full_version 0.8.2
%global pkgname yoke-derive-0.8

Name:           rust-yoke-derive-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "yoke-derive"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:de844c262c8848816172cef550288e7dc6c7b7814b4ee56b3e1553f275f1858e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.61
Requires:       crate(quote-1/default) >= 1.0.44
Requires:       crate(syn-2/default) >= 2.0.21
Requires:       crate(syn-2/fold) >= 2.0.21
Requires:       crate(synstructure-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "yoke-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
