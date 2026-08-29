# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minicbor-derive
%global full_version 0.13.0
%global pkgname minicbor-derive-0.13

Name:           rust-minicbor-derive-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "minicbor-derive"
License:        BlueOak-1.0.0
URL:            https://gitlab.com/twittner/minicbor
#!RemoteAsset:  sha256:1154809406efdb7982841adb6311b3d095b46f78342dd646736122fe6b19e267
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.18
Requires:       crate(quote-1/default) >= 1.0.7
Requires:       crate(syn-1/default) >= 1.0.72
Requires:       crate(syn-1/derive) >= 1.0.72
Requires:       crate(syn-1/extra-traits) >= 1.0.72
Requires:       crate(syn-1/visit) >= 1.0.72
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "minicbor-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
