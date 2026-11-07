# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quasi_macros
%global full_version 0.3.1
%global pkgname quasi-macros-0.3

Name:           rust-quasi-macros-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "quasi_macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-quasi
#!RemoteAsset:  sha256:875dd49ae93b74a25cb88dc00f6b35dc8c69b31ef8e8670468b0de976cfc9711
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quasi-codegen-0.3) >= 0.3.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Patch2000:      2000-Use-compatible-versioned-dependencies.patch

%description
Source code for takopackized Rust crate "quasi_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
