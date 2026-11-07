# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-sync
%global full_version 0.1.8
%global pkgname tokio-sync-0.1

Name:           rust-tokio-sync-0.1
Version:        0.1.8
Release:        %autorelease
Summary:        Rust crate "tokio-sync"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:edfe50152bc8164fcc456dab7891fa9bf8beaf01c5ee7e1dd43a397c3cf87dee
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1/default) >= 1.0.6
Requires:       crate(futures-0.1/default) >= 0.1.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-sync"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
