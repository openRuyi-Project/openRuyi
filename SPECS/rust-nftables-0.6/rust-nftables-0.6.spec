# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nftables
%global full_version 0.6.3
%global pkgname nftables-0.6

Name:           rust-nftables-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "nftables"
License:        MIT OR Apache-2.0
URL:            https://github.com/nftables-rs/nftables-rs
#!RemoteAsset:  sha256:3c57e7343eed9e9330e084eef12651b15be3c8ed7825915a0ffa33736b852bed
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(schemars-1/default) >= 1.0.4
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(serde-json-1/default) >= 1.0.142
Requires:       crate(serde-path-to-error-0.1/default) >= 0.1.0
Requires:       crate(strum-0.27/default) >= 0.27.2
Requires:       crate(strum-macros-0.27/default) >= 0.27.2
Requires:       crate(thiserror-2/default) >= 2.0.14
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
It can be used to create nftables rulesets in Rust and parse existing nftables rulesets from JSON.
Source code for takopackized Rust crate "nftables"

%package     -n %{name}+async-process
Summary:        Safe abstraction for nftables JSON API - feature "async-process"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-process-2/default) >= 2.4.0
Requires:       crate(futures-lite-2/default) >= 2.6.1
Provides:       crate(%{pkgname}/async-process) = %{version}

%description -n %{name}+async-process
It can be used to create nftables rulesets in Rust and parse existing nftables rulesets from JSON.
This metapackage enables feature "async-process" for the Rust nftables crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Safe abstraction for nftables JSON API - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.47.1
Requires:       crate(tokio-1/io-util) >= 1.47.1
Requires:       crate(tokio-1/process) >= 1.47.1
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
It can be used to create nftables rulesets in Rust and parse existing nftables rulesets from JSON.
This metapackage enables feature "tokio" for the Rust nftables crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
