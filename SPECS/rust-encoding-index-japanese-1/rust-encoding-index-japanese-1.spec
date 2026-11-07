# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encoding-index-japanese
%global full_version 1.20141219.5
%global pkgname encoding-index-japanese-1

Name:           rust-encoding-index-japanese-1
Version:        1.20141219.5
Release:        %autorelease
Summary:        Rust crate "encoding-index-japanese"
License:        CC0-1.0
URL:            https://github.com/lifthrasiir/rust-encoding
#!RemoteAsset:  sha256:04e8b2ff42e9a05335dbf8b5c6f7567e5591d0d916ccef4e0b1710d32a0d0c91
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(encoding-index-tests-0.1/default) >= 0.1.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "encoding-index-japanese"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
