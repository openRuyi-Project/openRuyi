# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name netlink-packet-core
%global full_version 0.8.1
%global pkgname netlink-packet-core-0.8

Name:           rust-netlink-packet-core-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "netlink-packet-core"
License:        MIT
URL:            https://github.com/rust-netlink/netlink-packet-core
#!RemoteAsset:  sha256:3463cbb78394cb0141e2c926b93fc2197e473394b761986eca3b9da2c63ae0f4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(paste-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "netlink-packet-core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
