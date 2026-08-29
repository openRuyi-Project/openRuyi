# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name socket2
%global full_version 0.4.10
%global pkgname socket2-0.4

Name:           rust-socket2-0.4
Version:        0.4.10
Release:        %autorelease
Summary:        Rust crate "socket2"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/socket2
#!RemoteAsset:  sha256:9f7916fc008ca5542385b89a3d3ce689953c143e9304a9bf8beec1de48994c0d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.149
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/handleapi) >= 0.3.9
Requires:       crate(winapi-0.3/ws2ipdef) >= 0.3.9
Requires:       crate(winapi-0.3/ws2tcpip) >= 0.3.9
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "socket2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
