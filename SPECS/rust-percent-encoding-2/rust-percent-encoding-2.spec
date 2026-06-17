# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name percent-encoding
%global full_version 2.3.2
%global pkgname percent-encoding-2

Name:           rust-percent-encoding-2
Version:        2.3.2
Release:        %autorelease
Summary:        Rust crate "percent-encoding"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url/
#!RemoteAsset:  sha256:9b4f627cb1b25917193a259e49bdad08f671f8d9708acfd5fe0a8c1455d87220
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "percent-encoding"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
