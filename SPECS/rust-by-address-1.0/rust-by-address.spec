# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name by_address
%global full_version 1.2.1
%global pkgname by-address-1.0

Name:           rust-by-address-1.0
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "by_address"
License:        MIT OR Apache-2.0
URL:            https://github.com/mbrubeck/by_address
#!RemoteAsset:  sha256:64fa3c856b712db6612c019f14756e64e4bcea13337a6b33b696333a9eaa2d06
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(by-address) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "by_address"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
