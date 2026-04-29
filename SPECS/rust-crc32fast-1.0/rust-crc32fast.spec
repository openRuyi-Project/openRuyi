# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crc32fast
%global full_version 1.5.0
%global pkgname crc32fast-1.0

Name:           rust-crc32fast-1.0
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "crc32fast"
License:        MIT OR Apache-2.0
URL:            https://github.com/srijs/rust-crc32fast
#!RemoteAsset:  sha256:9481c1c90cbf2ac953f07c8d4a58aa3945c425b7185c9154d67a65e4230da511
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "crc32fast"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
