# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name s3s-rfc2047
%global full_version 0.17.0
%global pkgname s3s-rfc2047-0.17

Name:           rust-s3s-rfc2047-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "s3s-rfc2047"
License:        Apache-2.0
URL:            https://github.com/Nugine/s3s
#!RemoteAsset:  sha256:918b207c39474baef4774355100e712dfea46020e3289ddd5b4bc6e21927b826
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-simd-0.8/default) >= 0.8.0
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "s3s-rfc2047"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
