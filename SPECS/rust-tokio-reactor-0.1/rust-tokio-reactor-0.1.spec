# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-reactor
%global full_version 0.1.12
%global pkgname tokio-reactor-0.1

Name:           rust-tokio-reactor-0.1
Version:        0.1.12
Release:        %autorelease
Summary:        Rust crate "tokio-reactor"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:09bc590ec4ba8ba87652da2068d150dcada2cfa2e07faae270a5e0409aa51351
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-utils-0.7/default) >= 0.7.0
Requires:       crate(futures-0.1/default) >= 0.1.19
Requires:       crate(lazy-static-1/default) >= 1.0.2
Requires:       crate(log-0.4/default) >= 0.4.1
Requires:       crate(mio-0.6/default) >= 0.6.14
Requires:       crate(num-cpus-1/default) >= 1.8.0
Requires:       crate(parking-lot-0.9/default) >= 0.9.0
Requires:       crate(slab-0.4/default) >= 0.4.0
Requires:       crate(tokio-executor-0.1/default) >= 0.1.1
Requires:       crate(tokio-io-0.1/default) >= 0.1.6
Requires:       crate(tokio-sync-0.1/default) >= 0.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-reactor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
