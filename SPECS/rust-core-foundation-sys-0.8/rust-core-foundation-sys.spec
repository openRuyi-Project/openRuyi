# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name core-foundation-sys
%global full_version 0.8.7
%global pkgname core-foundation-sys-0.8

Name:           rust-core-foundation-sys-0.8
Version:        0.8.7
Release:        %autorelease
Summary:        Rust crate "core-foundation-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/core-foundation-rs
#!RemoteAsset:  sha256:773648b94d0e5d620f64f280777445740e61fe701025087ec8b57f45c791888b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/link)
Provides:       crate(%{pkgname}/mac-os-10-7-support)
Provides:       crate(%{pkgname}/mac-os-10-8-features)

%description
Source code for takopackized Rust crate "core-foundation-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
