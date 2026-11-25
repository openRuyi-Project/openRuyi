# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bincode_derive-next
%global full_version 3.1.1
%global pkgname bincode-derive-next-3

Name:           rust-bincode-derive-next-3
Version:        3.1.1
Release:        %autorelease
Summary:        Rust crate "bincode_derive-next"
License:        MIT or Apache-2.0
URL:            https://github.com/Apich-Organization/bincode
#!RemoteAsset:  sha256:409532b1da3be643427e49c2f79e0c47d445f695e1b028270d9e80e9044d7d1c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(virtue-next-0.1/default) >= 0.1.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/static-size) = %{version}
Provides:       crate(%{pkgname}/zero-copy) = %{version}

%description
Source code for takopackized Rust crate "bincode_derive-next"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
