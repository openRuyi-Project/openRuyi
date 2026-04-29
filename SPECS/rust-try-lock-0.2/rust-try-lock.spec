# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name try-lock
%global full_version 0.2.5
%global pkgname try-lock-0.2

Name:           rust-try-lock-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "try-lock"
License:        MIT
URL:            https://github.com/seanmonstar/try-lock
#!RemoteAsset:  sha256:e421abadd41a4225275504ea4d6566923418b7f05506fbc9c0fe86ba7396114b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "try-lock"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
