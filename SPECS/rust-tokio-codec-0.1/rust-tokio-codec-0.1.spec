# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-codec
%global full_version 0.1.2
%global pkgname tokio-codec-0.1

Name:           rust-tokio-codec-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "tokio-codec"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:25b2998660ba0e70d18684de5d06b70b70a3a747469af9dea7618cc59e75976b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-0.4/default) >= 0.4.7
Requires:       crate(futures-0.1/default) >= 0.1.18
Requires:       crate(tokio-io-0.1/default) >= 0.1.7

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-codec"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
