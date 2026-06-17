# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name monostate
%global full_version 0.1.18
%global pkgname monostate-0.1

Name:           rust-monostate-0.1
Version:        0.1.18
Release:        %autorelease
Summary:        Rust crate "monostate"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/monostate
#!RemoteAsset:  sha256:3341a273f6c9d5bef1908f17b7267bbab0e95c9bf69a0d4dcf8e9e1b2c76ef67
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(monostate-impl-0.1/default) >= 0.1.18
Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1) >= 1.0.220
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "monostate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
