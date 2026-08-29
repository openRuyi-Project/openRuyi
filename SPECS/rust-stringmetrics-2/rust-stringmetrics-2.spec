# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stringmetrics
%global full_version 2.2.2
%global pkgname stringmetrics-2

Name:           rust-stringmetrics-2
Version:        2.2.2
Release:        %autorelease
Summary:        Rust crate "stringmetrics"
License:        FIXME
URL:            https://github.com/pluots/stringmetrics
#!RemoteAsset:  sha256:7b3c8667cd96245cbb600b8dec5680a7319edd719c5aa2b5d23c6bff94f39765
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "stringmetrics"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
