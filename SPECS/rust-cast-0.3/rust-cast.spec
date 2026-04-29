# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cast
%global full_version 0.3.0
%global pkgname cast-0.3

Name:           rust-cast-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "cast"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/cast.rs
#!RemoteAsset:  sha256:37b2a672a2cb129a2e41c10b1224bb368f9f37a2b16b612598138befd7b37eb5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "cast"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
