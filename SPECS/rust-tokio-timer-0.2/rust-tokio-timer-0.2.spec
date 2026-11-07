# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-timer
%global full_version 0.2.13
%global pkgname tokio-timer-0.2

Name:           rust-tokio-timer-0.2
Version:        0.2.13
Release:        %autorelease
Summary:        Rust crate "tokio-timer"
License:        MIT
URL:            https://github.com/tokio-rs/tokio
#!RemoteAsset:  sha256:93044f2d313c95ff1cb7809ce9a7a05735b012288a888b62d4434fd58c94f296
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-utils-0.7/default) >= 0.7.0
Requires:       crate(futures-0.1/default) >= 0.1.19
Requires:       crate(slab-0.4/default) >= 0.4.1
Requires:       crate(tokio-executor-0.1/default) >= 0.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-timer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
