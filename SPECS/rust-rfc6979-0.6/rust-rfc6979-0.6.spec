# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rfc6979
%global full_version 0.6.0
%global pkgname rfc6979-0.6

Name:           rust-rfc6979-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "rfc6979"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/rfc6979
#!RemoteAsset:  sha256:b4a459cddafb3fe76b31fd8f1108007566c40301feb64dc7b54656eb7388172b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-bigint-0.7) >= 0.7.5
Requires:       crate(hmac-0.13) >= 0.13.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rfc6979"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
