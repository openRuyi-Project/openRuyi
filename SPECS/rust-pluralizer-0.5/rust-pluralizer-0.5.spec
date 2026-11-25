# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pluralizer
%global full_version 0.5.0
%global pkgname pluralizer-0.5

Name:           rust-pluralizer-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "pluralizer"
License:        MIT OR Apache-2.0
URL:            https://github.com/KennethGomez/pluralizer
#!RemoteAsset:  sha256:4b3eba432a00a1f6c16f39147847a870e94e2e9b992759b503e330efec778cbe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.20.2
Requires:       crate(regex-1/default) >= 1.11.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pluralizer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
