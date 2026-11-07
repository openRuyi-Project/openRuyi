# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-io
%global full_version 0.1.13
%global pkgname tokio-io-0.1

Name:           rust-tokio-io-0.1
Version:        0.1.13
Release:        %autorelease
Summary:        Rust crate "tokio-io"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:57fc868aae093479e3131e3d165c93b1c7474109d13c90ec0dda2a1bbfff0674
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-0.4/default) >= 0.4.7
Requires:       crate(futures-0.1/default) >= 0.1.18
Requires:       crate(log-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-io"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
