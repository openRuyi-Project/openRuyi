# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fiat-crypto
%global full_version 0.2.9
%global pkgname fiat-crypto-0.2

Name:           rust-fiat-crypto-0.2
Version:        0.2.9
Release:        %autorelease
Summary:        Rust crate "fiat-crypto"
License:        MIT OR Apache-2.0 OR BSD-1-Clause
URL:            https://github.com/mit-plv/fiat-crypto
#!RemoteAsset:  sha256:28dea519a9695b9977216879a3ebfddf92f1c08c05d984f8996aecd6ecdc811d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "fiat-crypto"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
