# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name http
%global full_version 1.4.0
%global pkgname http-1.0

Name:           rust-http-1.0
Version:        1.4.0
Release:        %autorelease
Summary:        Rust crate "http"
License:        MIT OR Apache-2.0
URL:            https://github.com/hyperium/http
#!RemoteAsset:  sha256:e3ba2a386d7f85a81f119ad7498ebe444d2e22c2af0b86b069416ace48b3311a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1.0/default) >= 1.11.1
Requires:       crate(itoa-1.0/default) >= 1.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "http"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
