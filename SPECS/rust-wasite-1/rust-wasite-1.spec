# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasite
%global full_version 1.0.2
%global pkgname wasite-1

Name:           rust-wasite-1
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "wasite"
License:        Apache-2.0 OR BSL-1.0 OR MIT
URL:            https://github.com/ardaku/wasite/releases
#!RemoteAsset:  sha256:66fe902b4a6b8028a753d5424909b764ccf79b7a209eac9bf97e59cda9f71a42
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-range-dependencies.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(wasi-0.14) >= 0.14.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wasite"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
