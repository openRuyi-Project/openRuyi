# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name monostate-impl
%global full_version 0.1.18
%global pkgname monostate-impl-0.1

Name:           rust-monostate-impl-0.1
Version:        0.1.18
Release:        %autorelease
Summary:        Rust crate "monostate-impl"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/monostate
#!RemoteAsset:  sha256:e4db6d5580af57bf992f59068d4ea26fd518574ff48d7639b255a36f9de6e7e9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.105
Requires:       crate(quote-1.0/default) >= 1.0.43
Requires:       crate(syn-2.0/parsing) >= 2.0.114
Requires:       crate(syn-2.0/proc-macro) >= 2.0.114
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "monostate-impl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
