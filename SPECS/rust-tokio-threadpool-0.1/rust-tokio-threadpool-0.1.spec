# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-threadpool
%global full_version 0.1.18
%global pkgname tokio-threadpool-0.1

Name:           rust-tokio-threadpool-0.1
Version:        0.1.18
Release:        %autorelease
Summary:        Rust crate "tokio-threadpool"
License:        MIT
URL:            https://github.com/tokio-rs/tokio
#!RemoteAsset:  sha256:df720b6581784c118f0eb4310796b12b1d242a7eb95f716a8367855325c25f89
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-deque-0.7/default) >= 0.7.0
Requires:       crate(crossbeam-queue-0.2/default) >= 0.2.0
Requires:       crate(crossbeam-utils-0.7/default) >= 0.7.0
Requires:       crate(futures-0.1/default) >= 0.1.19
Requires:       crate(lazy-static-1/default) >= 1.0.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(num-cpus-1/default) >= 1.2.0
Requires:       crate(slab-0.4/default) >= 0.4.1
Requires:       crate(tokio-executor-0.1/default) >= 0.1.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-threadpool"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
