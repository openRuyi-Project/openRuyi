# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name percent-encoding
%global full_version 1.0.1
%global pkgname percent-encoding-1

Name:           rust-percent-encoding-1
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "percent-encoding"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url/
#!RemoteAsset:  sha256:31010dd2e1ac33d5b46a5b413495239882813e0369f8ed8a5e266f173602f831
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "percent-encoding"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
