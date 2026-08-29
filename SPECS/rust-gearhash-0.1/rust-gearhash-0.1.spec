# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gearhash
%global full_version 0.1.3
%global pkgname gearhash-0.1

Name:           rust-gearhash-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "gearhash"
License:        MIT OR Apache-2.0
URL:            https://github.com/srijs/rust-gearhash
#!RemoteAsset:  sha256:c8cf82cf76cd16485e56295a1377c775ce708c9f1a0be6b029076d60a245d213
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-0.1/default) >= 0.1.10
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gearhash"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
