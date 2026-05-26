# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name data-encoding
%global full_version 2.11.0
%global pkgname data-encoding-2.0

Name:           rust-data-encoding-2.0
Version:        2.11.0
Release:        %autorelease
Summary:        Rust crate "data-encoding"
License:        MIT
URL:            https://github.com/ia0/data-encoding
#!RemoteAsset:  sha256:a4ae5f15dda3c708c0ade84bfee31ccab44a3da4f88015ed22f63732abe300c8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(data-encoding) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "data-encoding"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
