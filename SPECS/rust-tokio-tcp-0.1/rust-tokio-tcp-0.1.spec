# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-tcp
%global full_version 0.1.4
%global pkgname tokio-tcp-0.1

Name:           rust-tokio-tcp-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "tokio-tcp"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:98df18ed66e3b72e742f185882a9e201892407957e45fbff8da17ae7a7c51f72
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-0.4/default) >= 0.4.0
Requires:       crate(futures-0.1/default) >= 0.1.19
Requires:       crate(iovec-0.1/default) >= 0.1.0
Requires:       crate(mio-0.6/default) >= 0.6.14
Requires:       crate(tokio-io-0.1/default) >= 0.1.6
Requires:       crate(tokio-reactor-0.1/default) >= 0.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-tcp"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
