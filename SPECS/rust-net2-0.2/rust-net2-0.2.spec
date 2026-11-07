# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name net2
%global full_version 0.2.39
%global pkgname net2-0.2

Name:           rust-net2-0.2
Version:        0.2.39
Release:        %autorelease
Summary:        Rust crate "net2"
License:        MIT OR Apache-2.0
URL:            https://github.com/deprecrated/net2-rs
#!RemoteAsset:  sha256:b13b648036a2339d06de780866fbdfda0dde886de7b3af2ddeba8b14f4ee34ac
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-0.1/default) >= 0.1.0
Requires:       crate(libc-0.2/default) >= 0.2.139
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/winsock2) >= 0.3.0
Requires:       crate(winapi-0.3/ws2def) >= 0.3.0
Requires:       crate(winapi-0.3/ws2ipdef) >= 0.3.0
Requires:       crate(winapi-0.3/ws2tcpip) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/duration) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "net2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
