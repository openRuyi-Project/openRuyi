# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tinyvec_macros
%global full_version 0.1.1
%global pkgname tinyvec-macros-0.1

Name:           rust-tinyvec-macros-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "tinyvec_macros"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/Soveu/tinyvec_macros
#!RemoteAsset:  sha256:1f3ccbac311fea05f86f61904b462b55fb3df8837a366dfc601a0161d0532f20
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tinyvec_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
