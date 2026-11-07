# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encoding-index-tradchinese
%global full_version 1.20141219.5
%global pkgname encoding-index-tradchinese-1

Name:           rust-encoding-index-tradchinese-1
Version:        1.20141219.5
Release:        %autorelease
Summary:        Rust crate "encoding-index-tradchinese"
License:        CC0-1.0
URL:            https://github.com/lifthrasiir/rust-encoding
#!RemoteAsset:  sha256:fd0e20d5688ce3cab59eb3ef3a2083a5c77bf496cb798dc6fcdb75f323890c18
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(encoding-index-tests-0.1/default) >= 0.1.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "encoding-index-tradchinese"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
