# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tiktoken-rs
%global full_version 0.7.0
%global pkgname tiktoken-rs-0.7

Name:           rust-tiktoken-rs-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "tiktoken-rs"
License:        MIT
URL:            https://github.com/zurawiki/tiktoken-rs
#!RemoteAsset:  sha256:25563eeba904d770acf527e8b370fe9a5547bacd20ff84a0b6c3bc41288e5625
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.98
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(bstr-1.0/default) >= 1.12.0
Requires:       crate(fancy-regex-0.13/default) >= 0.13.0
Requires:       crate(lazy-static-1.0/default) >= 1.5.0
Requires:       crate(regex-1.0/default) >= 1.11.1
Requires:       crate(rustc-hash-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tiktoken-rs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
