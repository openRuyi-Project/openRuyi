# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encoding-index-singlebyte
%global full_version 1.20141219.5
%global pkgname encoding-index-singlebyte-1

Name:           rust-encoding-index-singlebyte-1
Version:        1.20141219.5
Release:        %autorelease
Summary:        Rust crate "encoding-index-singlebyte"
License:        CC0-1.0
URL:            https://github.com/lifthrasiir/rust-encoding
#!RemoteAsset:  sha256:3351d5acffb224af9ca265f435b859c7c01537c0849754d3db3fdf2bfe2ae84a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(encoding-index-tests-0.1/default) >= 0.1.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "encoding-index-singlebyte"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
