# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name execute
%global full_version 0.2.13
%global pkgname execute-0.2

Name:           rust-execute-0.2
Version:        0.2.13
Release:        %autorelease
Summary:        Rust crate "execute"
License:        MIT
URL:            https://magiclen.org/execute
#!RemoteAsset:  sha256:3a82608ee96ce76aeab659e9b8d3c2b787bffd223199af88c674923d861ada10
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(execute-command-macro-0.1/default) >= 0.1.1
Requires:       crate(execute-command-tokens-0.1/default) >= 0.1.0
Requires:       crate(generic-array-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "execute"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
