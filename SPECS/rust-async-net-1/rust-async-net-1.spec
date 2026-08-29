# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-net
%global full_version 1.8.0
%global pkgname async-net-1

Name:           rust-async-net-1
Version:        1.8.0
Release:        %autorelease
Summary:        Rust crate "async-net"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-net
#!RemoteAsset:  sha256:0434b1ed18ce1cf5769b8ac540e33f01fa9471058b5e89da9e06f3c882a8c12f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-io-1/default) >= 1.6.0
Requires:       crate(blocking-1/default) >= 1.0.0
Requires:       crate(futures-lite-1/default) >= 1.11.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-net"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
