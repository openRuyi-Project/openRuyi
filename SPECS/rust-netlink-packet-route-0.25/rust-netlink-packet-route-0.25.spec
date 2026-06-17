# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name netlink-packet-route
%global full_version 0.25.1
%global pkgname netlink-packet-route-0.25

Name:           rust-netlink-packet-route-0.25
Version:        0.25.1
Release:        %autorelease
Summary:        Rust crate "netlink-packet-route"
License:        MIT
URL:            https://github.com/rust-netlink/netlink-packet-route
#!RemoteAsset:  sha256:3ec2f5b6839be2a19d7fa5aab5bc444380f6311c2b693551cb80f45caaa7b5ef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(libc-0.2/default) >= 0.2.66
Requires:       crate(log-0.4/default) >= 0.4.20
Requires:       crate(log-0.4/std) >= 0.4.20
Requires:       crate(netlink-packet-core-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rich-nlas) = %{version}

%description
Source code for takopackized Rust crate "netlink-packet-route"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
