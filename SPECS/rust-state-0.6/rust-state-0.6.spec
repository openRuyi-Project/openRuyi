# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name state
%global full_version 0.6.0
%global pkgname state-0.6

Name:           rust-state-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "state"
License:        MIT OR Apache-2.0
URL:            https://github.com/SergioBenitez/state
#!RemoteAsset:  sha256:2b8c4a4445d81357df8b1a650d0d0d6fbbbfe99d064aa5e02f3e4022061476d8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(loom-0.5/checkpoint) >= 0.5.0
Requires:       crate(loom-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/tls) = %{version}

%description
Source code for takopackized Rust crate "state"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
