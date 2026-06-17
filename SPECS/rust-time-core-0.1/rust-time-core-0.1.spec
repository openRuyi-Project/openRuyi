# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name time-core
%global full_version 0.1.8
%global pkgname time-core-0.1

Name:           rust-time-core-0.1
Version:        0.1.8
Release:        %autorelease
Summary:        Rust crate "time-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/time-rs/time
#!RemoteAsset:  sha256:7694e1cfe791f8d31026952abf09c69ca6f6fa4e1a1229e18988f06a04a12dca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/large-dates) = %{version}

%description
Source code for takopackized Rust crate "time-core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
