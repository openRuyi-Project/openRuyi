# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quick-error
%global full_version 1.2.0
%global pkgname quick-error-1

Name:           rust-quick-error-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "quick-error"
License:        MIT OR Apache-2.0
URL:            http://github.com/tailhook/quick-error
#!RemoteAsset:  sha256:3c36987d4978eb1be2e422b1e0423a557923a5c3e7e6f31d5699e9aafaefa469
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "quick-error"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
