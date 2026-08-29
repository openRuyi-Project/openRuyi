# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ucd-util
%global full_version 0.1.0
%global pkgname ucd-util-0.1

Name:           rust-ucd-util-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "ucd-util"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/rucd
#!RemoteAsset:  sha256:3ac9567e27ca9fc45bac22f987fd62547b0ac65d2e6502dfc09cdab7dbdba31f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ucd-util"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
