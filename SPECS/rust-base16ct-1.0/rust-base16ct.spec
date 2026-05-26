# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name base16ct
%global full_version 1.0.0
%global pkgname base16ct-1.0

Name:           rust-base16ct-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "base16ct"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/base16ct
#!RemoteAsset:  sha256:fd307490d624467aa6f74b0eabb77633d1f758a7b25f12bceb0b22e08d9726f6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(base16ct) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "base16ct"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
