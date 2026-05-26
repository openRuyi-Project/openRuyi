# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cmov
%global full_version 0.5.3
%global pkgname cmov-0.5

Name:           rust-cmov-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "cmov"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:3f88a43d011fc4a6876cb7344703e297c71dda42494fee094d5f7c76bf13f746
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(cmov) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Provides wrappers for the CMOV family of instructions on x86/x86_64 and CSEL on AArch64, along with a portable "best-effort" pure Rust fallback implementation.
Source code for takopackized Rust crate "cmov"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
