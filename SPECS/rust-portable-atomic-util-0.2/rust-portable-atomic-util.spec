# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name portable-atomic-util
%global full_version 0.2.6
%global pkgname portable-atomic-util-0.2

Name:           rust-portable-atomic-util-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "portable-atomic-util"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/portable-atomic-util
#!RemoteAsset:  sha256:091397be61a01d4be58e7841595bd4bfedb15f1cd54977d79b8271e94ed799a3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(portable-atomic-1.0/require-cas) >= 1.13.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "portable-atomic-util"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
