# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crc32fast
%global full_version 1.5.0
%global pkgname crc32fast-1

Name:           rust-crc32fast-1
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "crc32fast"
License:        MIT OR Apache-2.0
URL:            https://github.com/srijs/rust-crc32fast
#!RemoteAsset:  sha256:9481c1c90cbf2ac953f07c8d4a58aa3945c425b7185c9154d67a65e4230da511
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "crc32fast"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
