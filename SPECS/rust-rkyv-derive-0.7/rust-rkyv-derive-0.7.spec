# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rkyv_derive
%global full_version 0.7.46
%global pkgname rkyv-derive-0.7

Name:           rust-rkyv-derive-0.7
Version:        0.7.46
Release:        %autorelease
Summary:        Rust crate "rkyv_derive"
License:        MIT
URL:            https://github.com/rkyv/rkyv
#!RemoteAsset:  sha256:84d7b42d4b8d06048d3ac8db0eb31bcb942cbeb709f0b5f2b2ebde398d3038f5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/arbitrary-enum-discriminant) = %{version}
Provides:       crate(%{pkgname}/archive-be) = %{version}
Provides:       crate(%{pkgname}/archive-le) = %{version}
Provides:       crate(%{pkgname}/copy) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/strict) = %{version}

%description
Source code for takopackized Rust crate "rkyv_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
