# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name base-x
%global full_version 0.2.11
%global pkgname base-x-0.2

Name:           rust-base-x-0.2
Version:        0.2.11
Release:        %autorelease
Summary:        Rust crate "base-x"
License:        MIT
URL:            https://github.com/OrKoN/base-x-rs
#!RemoteAsset:  sha256:4cbbc9d0964165b47557570cce6c952866c2678457aca742aafc9fb771d30270
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "base-x"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
