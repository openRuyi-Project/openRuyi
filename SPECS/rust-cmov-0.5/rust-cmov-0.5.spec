# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cmov
%global full_version 0.5.4
%global pkgname cmov-0.5

Name:           rust-cmov-0.5
Version:        0.5.4
Release:        %autorelease
Summary:        Rust crate "cmov"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:0c9ea0ac24bc397ab3c98583a3c9ba74fa56b09a4449bbe172b9b1ddb016027a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Provides wrappers for the CMOV family of instructions on x86/x86_64 and CSEL on AArch64, along with a portable "best-effort" pure Rust fallback implementation.
Source code for takopackized Rust crate "cmov"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
