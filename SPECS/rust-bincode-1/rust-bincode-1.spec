# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bincode
%global full_version 1.3.3
%global pkgname bincode-1

Name:           rust-bincode-1
Version:        1.3.3
Release:        %autorelease
Summary:        Rust crate "bincode"
License:        MIT
URL:            https://github.com/servo/bincode
#!RemoteAsset:  sha256:b1f45e9417d87227c7a56d22e471c6206462cba514c7590c09aff4cf6d1ddcad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.63
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/i128) = %{version}

%description
Source code for takopackized Rust crate "bincode"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
