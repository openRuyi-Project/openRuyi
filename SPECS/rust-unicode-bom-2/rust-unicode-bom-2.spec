# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-bom
%global full_version 2.0.3
%global pkgname unicode-bom-2

Name:           rust-unicode-bom-2
Version:        2.0.3
Release:        %autorelease
Summary:        Rust crate "unicode-bom"
License:        Apache-2.0
URL:            https://gitlab.com/philbooth/unicode-bom
#!RemoteAsset:  sha256:7eec5d1121208364f6793f7d2e222bf75a915c19557537745b195b253dd64217
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unicode-bom"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
