# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_path_to_error
%global full_version 0.1.20
%global pkgname serde-path-to-error-0.1

Name:           rust-serde-path-to-error-0.1
Version:        0.1.20
Release:        %autorelease
Summary:        Rust crate "serde_path_to_error"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/path-to-error
#!RemoteAsset:  sha256:10a9ff822e371bb5403e391ecd83e182e0e77ba7f6fe0160b795797109d1b457
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1/alloc) >= 1.0.220
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_path_to_error"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
