# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitfields
%global full_version 1.0.2
%global pkgname bitfields-1

Name:           rust-bitfields-1
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "bitfields"
License:        MIT
URL:            https://github.com/gregorygaines/bitfields-rs
#!RemoteAsset:  sha256:d866f92dc1574aa8da443eacb06ad8fbe4056dbc1b7c3aae508cbccd46c7e706
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitfields-impl-1/default) >= 1.0.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Useful for low-level code (embedded or emulators).
Source code for takopackized Rust crate "bitfields"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
