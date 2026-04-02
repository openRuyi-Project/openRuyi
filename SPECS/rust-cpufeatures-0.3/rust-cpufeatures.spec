# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cpufeatures
%global full_version 0.3.0
%global pkgname cpufeatures-0.3

Name:           rust-cpufeatures-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "cpufeatures"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:8b2a41393f66f16b0823bb79094d54ac5fbd34ab292ddafb9a0456ac9f87d201
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.184
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cpufeatures"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
