# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name resolv-conf
%global full_version 0.7.6
%global pkgname resolv-conf-0.7

Name:           rust-resolv-conf-0.7
Version:        0.7.6
Release:        %autorelease
Summary:        Rust crate "resolv-conf"
License:        MIT OR Apache-2.0
URL:            https://github.com/hickory-dns/resolv-conf
#!RemoteAsset:  sha256:1e061d1b48cb8d38042de4ae0a7a6401009d6143dc80d2e2d6f31f0bdd6470c7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/system) = %{version}
Obsoletes:      %{name}+hostname < %{version}

%description
Source code for takopackized Rust crate "resolv-conf"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
