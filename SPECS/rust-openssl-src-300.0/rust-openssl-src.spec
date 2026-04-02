# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssl-src
%global full_version 300.5.5+3.5.5
%global pkgname openssl-src-300.0

Name:           rust-openssl-src-300.0
Version:        300.5.5
Release:        %autorelease
Summary:        Rust crate "openssl-src"
License:        MIT/Apache-2.0
URL:            https://github.com/alexcrichton/openssl-src-rs
#!RemoteAsset:  sha256:3f1787d533e03597a7934fd0a765f0d28e94ecc5fb7789f8053b1e699a56f709
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.58
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/camellia)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/force-engine)
Provides:       crate(%{pkgname}/idea)
Provides:       crate(%{pkgname}/ktls)
Provides:       crate(%{pkgname}/legacy)
Provides:       crate(%{pkgname}/no-dso)
Provides:       crate(%{pkgname}/seed)
Provides:       crate(%{pkgname}/ssl3)
Provides:       crate(%{pkgname}/weak-crypto)

%description
Source code for takopackized Rust crate "openssl-src"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
