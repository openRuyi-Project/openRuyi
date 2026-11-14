# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-io-timeout
%global full_version 1.2.1
%global pkgname tokio-io-timeout-1

Name:           rust-tokio-io-timeout-1
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "tokio-io-timeout"
License:        MIT OR Apache-2.0
URL:            https://github.com/sfackler/tokio-io-timeout
#!RemoteAsset:  sha256:0bd86198d9ee903fedd2f9a2e72014287c0d9167e4ae43b5853007205dda1b76
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-io-timeout"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
