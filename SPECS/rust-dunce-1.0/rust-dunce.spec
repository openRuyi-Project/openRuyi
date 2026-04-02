# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dunce
%global full_version 1.0.5
%global pkgname dunce-1.0

Name:           rust-dunce-1.0
Version:        1.0.5
Release:        %autorelease
Summary:        Rust crate "dunce"
License:        CC0-1.0 OR MIT-0 OR Apache-2.0
URL:            https://lib.rs/crates/dunce
#!RemoteAsset:  sha256:92773504d58c093f6de2459af4af33faa518c13451eb8f2b5698ed3d36e7c813
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "dunce"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
