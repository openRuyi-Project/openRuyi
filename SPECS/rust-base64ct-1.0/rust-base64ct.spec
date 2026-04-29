# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name base64ct
%global full_version 1.8.3
%global pkgname base64ct-1.0

Name:           rust-base64ct-1.0
Version:        1.8.3
Release:        %autorelease
Summary:        Rust crate "base64ct"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/base64ct
#!RemoteAsset:  sha256:2af50177e190e07a26ab74f8b1efbfe2ef87da2116221318cb1c2e82baf7de06
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "base64ct"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
