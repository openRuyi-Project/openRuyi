# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ntest
%global full_version 0.9.5
%global pkgname ntest-0.9

Name:           rust-ntest-0.9
Version:        0.9.5
Release:        %autorelease
Summary:        Rust crate "ntest"
License:        MIT
URL:            https://github.com/becheran/ntest
#!RemoteAsset:  sha256:54d1aa56874c2152c24681ed0df95ee155cc06c5c61b78e2d1e8c0cae8bc5326
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ntest-test-cases-0.9/default) >= 0.9.5
Requires:       crate(ntest-timeout-0.9/default) >= 0.9.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ntest"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
