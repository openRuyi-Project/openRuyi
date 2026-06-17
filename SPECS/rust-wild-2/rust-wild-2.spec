# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wild
%global full_version 2.2.1
%global pkgname wild-2

Name:           rust-wild-2
Version:        2.2.1
Release:        %autorelease
Summary:        Rust crate "wild"
License:        Apache-2.0 OR MIT
URL:            https://lib.rs/crates/wild
#!RemoteAsset:  sha256:a3131afc8c575281e1e80f36ed6a092aa502c08b18ed7524e86fbbb12bb410e1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glob-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/glob-quoted-on-windows) = %{version}

%description
Source code for takopackized Rust crate "wild"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
