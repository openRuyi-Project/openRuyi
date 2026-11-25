# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name as-any
%global full_version 0.3.2
%global pkgname as-any-0.3

Name:           rust-as-any-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "as-any"
License:        MIT OR Apache-2.0
URL:            https://codeberg.org/fogti/as-any
#!RemoteAsset:  sha256:b0f477b951e452a0b6b4a10b53ccd569042d1d01729b519e02074a9c0958a063
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "as-any"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
