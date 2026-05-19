# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lsp-server
%global full_version 0.7.9
%global pkgname lsp-server-0.7

Name:           rust-lsp-server-0.7
Version:        0.7.9
Release:        %autorelease
Summary:        Rust crate "lsp-server"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/rust-analyzer/tree/master/lib/lsp-server
#!RemoteAsset:  sha256:7d6ada348dbc2703cbe7637b2dda05cff84d3da2819c24abcb305dd613e0ba2e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.15
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-derive-1.0/default) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "lsp-server"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
