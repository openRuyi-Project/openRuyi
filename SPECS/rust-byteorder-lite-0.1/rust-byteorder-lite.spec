# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name byteorder-lite
%global full_version 0.1.0
%global pkgname byteorder-lite-0.1

Name:           rust-byteorder-lite-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "byteorder-lite"
License:        Unlicense OR MIT
URL:            https://github.com/image-rs/byteorder-lite
#!RemoteAsset:  sha256:8f1fe948ff07f4bd06c30984e69f5b4899c516a3ef74f34df92a2df2ab535495
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(byteorder-lite) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "byteorder-lite"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
