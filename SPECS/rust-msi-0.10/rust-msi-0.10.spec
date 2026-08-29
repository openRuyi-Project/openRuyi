# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name msi
%global full_version 0.10.0
%global pkgname msi-0.10

Name:           rust-msi-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "msi"
License:        MIT
URL:            https://github.com/mdsteele/rust-msi
#!RemoteAsset:  sha256:b0325f8473ef1f5c38ee42345e2cd1678299cbbfa169d1776654a2a682867420
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.0.0
Requires:       crate(cfb-0.14/default) >= 0.14.0
Requires:       crate(encoding-rs-0.8/default) >= 0.8.0
Requires:       crate(uuid-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "msi"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
