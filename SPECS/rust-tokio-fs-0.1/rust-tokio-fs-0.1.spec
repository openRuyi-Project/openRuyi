# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-fs
%global full_version 0.1.7
%global pkgname tokio-fs-0.1

Name:           rust-tokio-fs-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "tokio-fs"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:297a1206e0ca6302a0eed35b700d292b275256f596e2f3fea7729d5e629b6ff4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-0.1/default) >= 0.1.21
Requires:       crate(tokio-io-0.1/default) >= 0.1.6
Requires:       crate(tokio-threadpool-0.1/default) >= 0.1.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-fs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
