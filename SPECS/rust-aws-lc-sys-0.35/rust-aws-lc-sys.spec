# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aws-lc-sys
%global full_version 0.35.0
%global pkgname aws-lc-sys-0.35

Name:           rust-aws-lc-sys-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "aws-lc-sys"
License:        ISC AND (Apache-2.0 OR ISC) AND OpenSSL
URL:            https://github.com/aws/aws-lc-rs
#!RemoteAsset:  sha256:b45afffdee1e7c9126814751f88dddc747f41d91da16c9551a0f1e8a11e788a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.52
Requires:       crate(cc-1.0/parallel) >= 1.2.52
Requires:       crate(cmake-0.1/default) >= 0.1.57
Requires:       crate(dunce-1.0/default) >= 1.0.5
Requires:       crate(fs-extra-1.0/default) >= 1.3.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/all-bindings)
Provides:       crate(%{pkgname}/asan)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/prebuilt-nasm)

%description
It іs based on code from the Google BoringSSL project and the OpenSSL project.
Source code for takopackized Rust crate "aws-lc-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
