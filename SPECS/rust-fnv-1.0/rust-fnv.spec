# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fnv
%global full_version 1.0.7
%global pkgname fnv-1.0

Name:           rust-fnv-1.0
Version:        1.0.7
Release:        %autorelease
Summary:        Rust crate "fnv"
License:        Apache-2.0 / MIT
URL:            https://github.com/servo/rust-fnv
#!RemoteAsset:  sha256:3f9eec918d3f24069decb9af1554cad7c880e2da24a9afd88aca000531ab82c1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "fnv"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
