# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name endi
%global full_version 1.1.1
%global pkgname endi-1

Name:           rust-endi-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "endi"
License:        MIT
URL:            https://github.com/zeenix/endi
#!RemoteAsset:  sha256:66b7e2430c6dff6a955451e2cfc438f09cea1965a9d6f87f7e3b90decc014099
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "endi"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
