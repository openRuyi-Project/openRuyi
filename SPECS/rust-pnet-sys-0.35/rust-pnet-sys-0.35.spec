# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pnet_sys
%global full_version 0.35.0
%global pkgname pnet-sys-0.35

Name:           rust-pnet-sys-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "pnet_sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/libpnet/libpnet
#!RemoteAsset:  sha256:7d4643d3d4db6b08741050c2f3afa9a892c4244c085a72fcda93c9c2c9a00f4b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.147
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/winsock2) >= 0.3.9
Requires:       crate(winapi-0.3/ws2ipdef) >= 0.3.9
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pnet_sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
