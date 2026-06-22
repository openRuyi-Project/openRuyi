# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_regex
%global full_version 1.2.0
%global pkgname serde-regex-1

Name:           rust-serde-regex-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "serde_regex"
License:        MIT OR Apache-2.0
URL:            https://github.com/tailhook/serde-regex
#!RemoteAsset:  sha256:bafc8d0c5330cecff10f16b459b479fd9acaa5b4acd7167301414e21b0057012
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(regex-1/default) >= 1.5.5
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_regex"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
