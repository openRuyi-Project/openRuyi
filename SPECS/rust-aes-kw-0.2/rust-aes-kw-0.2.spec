# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aes-kw
%global full_version 0.2.1
%global pkgname aes-kw-0.2

Name:           rust-aes-kw-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "aes-kw"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/key-wraps/
#!RemoteAsset:  sha256:69fa2b352dcefb5f7f3a5fb840e02665d311d878955380515e4fd50095dd3d8c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aes-0.8/default) >= 0.8.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "aes-kw"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
