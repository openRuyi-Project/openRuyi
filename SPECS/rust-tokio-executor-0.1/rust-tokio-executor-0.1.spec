# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-executor
%global full_version 0.1.10
%global pkgname tokio-executor-0.1

Name:           rust-tokio-executor-0.1
Version:        0.1.10
Release:        %autorelease
Summary:        Rust crate "tokio-executor"
License:        MIT
URL:            https://github.com/tokio-rs/tokio
#!RemoteAsset:  sha256:fb2d1b8f4548dbf5e1f7818512e9c406860678f29c300cdf0ebac72d1a3a1671
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-utils-0.7/default) >= 0.7.0
Requires:       crate(futures-0.1/default) >= 0.1.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-executor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
