# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name netlink-packet-core
%global full_version 0.9.0
%global pkgname netlink-packet-core-0.9

Name:           rust-netlink-packet-core-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "netlink-packet-core"
License:        MIT
URL:            https://github.com/rust-netlink/netlink-packet-core
#!RemoteAsset:  sha256:2d6e2daf9a8c2e21302714706860a0e6be02e03d17294ecc66b354ea7d4059dd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "netlink-packet-core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
