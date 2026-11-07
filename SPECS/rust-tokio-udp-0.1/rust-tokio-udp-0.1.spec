# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-udp
%global full_version 0.1.6
%global pkgname tokio-udp-0.1

Name:           rust-tokio-udp-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "tokio-udp"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:e2a0b10e610b39c38b031a2fcab08e4b82f16ece36504988dcbd81dbba650d82
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-0.4/default) >= 0.4.0
Requires:       crate(futures-0.1/default) >= 0.1.19
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(mio-0.6/default) >= 0.6.14
Requires:       crate(tokio-codec-0.1/default) >= 0.1.0
Requires:       crate(tokio-io-0.1/default) >= 0.1.7
Requires:       crate(tokio-reactor-0.1/default) >= 0.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-udp"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
