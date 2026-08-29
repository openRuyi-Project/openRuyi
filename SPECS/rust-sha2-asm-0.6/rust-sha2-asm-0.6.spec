# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha2-asm
%global full_version 0.6.4
%global pkgname sha2-asm-0.6

Name:           rust-sha2-asm-0.6
Version:        0.6.4
Release:        %autorelease
Summary:        Rust crate "sha2-asm"
License:        MIT
URL:            https://github.com/RustCrypto/asm-hashes
#!RemoteAsset:  sha256:b845214d6175804686b2bd482bcffe96651bb2d1200742b712003504a2dac1ab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sha2-asm"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
