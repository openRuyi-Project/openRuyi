# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cloudflare-zlib-sys
%global full_version 0.3.7
%global pkgname cloudflare-zlib-sys-0.3

Name:           rust-cloudflare-zlib-sys-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "cloudflare-zlib-sys"
License:        Zlib
URL:            https://lib.rs/crates/cloudflare-zlib-sys
#!RemoteAsset:  sha256:d11ad9b1a14235a8ce48c2622c57fde45c3f8e7d29344775583a847d245360be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/asm) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cloudflare-zlib-sys"

%files
%license LICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
