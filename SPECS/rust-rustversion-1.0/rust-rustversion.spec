# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustversion
%global full_version 1.0.22
%global pkgname rustversion-1.0

Name:           rust-rustversion-1.0
Version:        1.0.22
Release:        %autorelease
Summary:        Rust crate "rustversion"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/rustversion
#!RemoteAsset:  sha256:b39cdef0fa800fc44525c84ccb54a029961a8215f9619753635a9c0d2538d46d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "rustversion"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
