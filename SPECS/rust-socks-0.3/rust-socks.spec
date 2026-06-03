# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name socks
%global full_version 0.3.4
%global pkgname socks-0.3

Name:           rust-socks-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "socks"
License:        MIT OR Apache-2.0
URL:            https://github.com/sfackler/rust-socks
#!RemoteAsset:  sha256:f0c3dbbd9ae980613c6dd8e28a9407b50509d3803b57624d5dfe8315218cd58b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1.0/default) >= 1.5.0
Requires:       crate(libc-0.2/default) >= 0.2.180
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/winsock2) >= 0.3.9
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "socks"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
