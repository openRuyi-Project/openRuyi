# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libnghttp2-sys
%global full_version 0.1.13+1.68.1
%global pkgname libnghttp2-sys-0.1

Name:           rust-libnghttp2-sys-0.1
Version:        0.1.13
Release:        %autorelease
Summary:        Rust crate "libnghttp2-sys"
License:        MIT/Apache-2.0
URL:            https://github.com/alexcrichton/nghttp2-rs
#!RemoteAsset:  sha256:492e00167f1418c15648144f42bbfc63099806ecee9bf8d09a6353d6b4856b3c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.58
Requires:       crate(libc-0.2/default) >= 0.2.184
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "libnghttp2-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
