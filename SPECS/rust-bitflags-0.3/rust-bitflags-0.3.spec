# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitflags
%global full_version 0.3.3
%global pkgname bitflags-0.3

Name:           rust-bitflags-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "bitflags"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/bitflags
#!RemoteAsset:  sha256:32866f4d103c4e438b1db1158aa1b1a80ee078e5d77a59a2f906fd62a577389c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bitflags"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
