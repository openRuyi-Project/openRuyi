# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git-version-macro
%global full_version 0.3.9
%global pkgname git-version-macro-0.3

Name:           rust-git-version-macro-0.3
Version:        0.3.9
Release:        %autorelease
Summary:        Rust crate "git-version-macro"
License:        BSD-2-Clause
URL:            https://github.com/fusion-engineering/rust-git-version
#!RemoteAsset:  sha256:53010ccb100b96a67bc32c0175f0ed1426b31b655d562898e57325f81c023ac0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "git-version-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
