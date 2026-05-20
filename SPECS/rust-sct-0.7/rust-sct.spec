# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sct
%global full_version 0.7.1
%global pkgname sct-0.7

Name:           rust-sct-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "sct"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/rustls/sct.rs
#!RemoteAsset:  sha256:da046153aa2352493d6cb7da4b6e5c0c057d8a1d0a9aa8560baffdd945acd414
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ring-0.17/default) >= 0.17.0
Requires:       crate(untrusted-0.9/default) >= 0.9.0
Provides:       crate(sct) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "sct"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
