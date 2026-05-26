# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name avif-serialize
%global full_version 0.8.9
%global pkgname avif-serialize-0.8

Name:           rust-avif-serialize-0.8
Version:        0.8.9
Release:        %autorelease
Summary:        Rust crate "avif-serialize"
License:        BSD-3-Clause
URL:            https://lib.rs/avif-serialize
#!RemoteAsset:  sha256:e7178fe5f7d460b13895ebb9dcb28a3a6216d2df2574a0806cb51b555d297f38
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7/default) >= 0.7.6
Provides:       crate(avif-serialize) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "avif-serialize"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
