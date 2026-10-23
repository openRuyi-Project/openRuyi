# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name to_method
%global full_version 1.1.0
%global pkgname to-method-1

Name:           rust-to-method-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "to_method"
License:        CC0-1.0
URL:            https://github.com/whentze/to_method
#!RemoteAsset:  sha256:c7c4ceeeca15c8384bbc3e011dbd8fccb7f068a440b752b7d9b32ceb0ca0e2e8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "to_method"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
