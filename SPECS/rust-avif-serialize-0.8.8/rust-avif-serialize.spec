# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name avif-serialize
%global full_version 0.8.8
%global pkgname avif-serialize-0.8.8

Name:           rust-avif-serialize-0.8.8
Version:        0.8.8
Release:        %autorelease
Summary:        Rust crate "avif-serialize"
License:        BSD-3-Clause
URL:            https://lib.rs/avif-serialize
#!RemoteAsset:  sha256:375082f007bd67184fb9c0374614b29f9aaa604ec301635f72338bb65386a53d
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
