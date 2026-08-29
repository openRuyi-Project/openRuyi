# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssl-probe
%global full_version 0.2.1
%global pkgname openssl-probe-0.2

Name:           rust-openssl-probe-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "openssl-probe"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustls/openssl-probe
#!RemoteAsset:  sha256:7c87def4c32ab89d880effc9e097653c8da5d6ef28e6b539d313baaacfbafcbe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "openssl-probe"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
