# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tikv-jemalloc-sys
%global full_version 0.6.1+5.3.0-1-ge13ca993e8ccb9ba9847cc330696e02839f328f7
%global pkgname tikv-jemalloc-sys-0.6

Name:           rust-tikv-jemalloc-sys-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "tikv-jemalloc-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/tikv/jemallocator
#!RemoteAsset:  sha256:cd8aa5b2ab86a2cefa406d889139c162cbb230092f7d1d7cbc1716405d852a3b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.13
Requires:       crate(libc-0.2) >= 0.2.8
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/background-threads) = %{version}
Provides:       crate(%{pkgname}/background-threads-runtime-support) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/disable-cache-oblivious) = %{version}
Provides:       crate(%{pkgname}/disable-initial-exec-tls) = %{version}
Provides:       crate(%{pkgname}/override-allocator-on-supported-platforms) = %{version}
Provides:       crate(%{pkgname}/profiling) = %{version}
Provides:       crate(%{pkgname}/stats) = %{version}
Provides:       crate(%{pkgname}/unprefixed-malloc-on-supported-platforms) = %{version}

%description
Source code for takopackized Rust crate "tikv-jemalloc-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
