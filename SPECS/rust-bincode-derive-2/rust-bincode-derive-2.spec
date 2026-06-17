# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bincode_derive
%global full_version 2.0.1
%global pkgname bincode-derive-2

Name:           rust-bincode-derive-2
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "bincode_derive"
License:        MIT
URL:            https://github.com/bincode-org/bincode
#!RemoteAsset:  sha256:bf95709a440f45e986983918d0e8a1f30a9b1df04918fc828670606804ac3c09
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(virtue-0.0.18/default) >= 0.0.18
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bincode_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
