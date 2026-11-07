# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encoding-index-korean
%global full_version 1.20141219.5
%global pkgname encoding-index-korean-1

Name:           rust-encoding-index-korean-1
Version:        1.20141219.5
Release:        %autorelease
Summary:        Rust crate "encoding-index-korean"
License:        CC0-1.0
URL:            https://github.com/lifthrasiir/rust-encoding
#!RemoteAsset:  sha256:4dc33fb8e6bcba213fe2f14275f0963fd16f0a02c878e3095ecfdf5bee529d81
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(encoding-index-tests-0.1/default) >= 0.1.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "encoding-index-korean"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
