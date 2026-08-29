# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-fs
%global full_version 1.6.0
%global pkgname async-fs-1

Name:           rust-async-fs-1
Version:        1.6.0
Release:        %autorelease
Summary:        Rust crate "async-fs"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-fs
#!RemoteAsset:  sha256:279cf904654eeebfa37ac9bb1598880884924aab82e290aa65c9e77a0e142e06
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-lock-2/default) >= 2.3.0
Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(blocking-1/default) >= 1.0.0
Requires:       crate(futures-lite-1/default) >= 1.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-fs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
