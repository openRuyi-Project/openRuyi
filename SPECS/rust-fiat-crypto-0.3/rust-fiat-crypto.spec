# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fiat-crypto
%global full_version 0.3.0
%global pkgname fiat-crypto-0.3

Name:           rust-fiat-crypto-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "fiat-crypto"
License:        MIT OR Apache-2.0 OR BSD-1-Clause
URL:            https://github.com/mit-plv/fiat-crypto
#!RemoteAsset:  sha256:64cd1e32ddd350061ae6edb1b082d7c54915b5c672c389143b9a63403a109f24
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "fiat-crypto"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
