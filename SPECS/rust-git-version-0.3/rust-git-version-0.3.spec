# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git-version
%global full_version 0.3.9
%global pkgname git-version-0.3

Name:           rust-git-version-0.3
Version:        0.3.9
Release:        %autorelease
Summary:        Rust crate "git-version"
License:        BSD-2-Clause
URL:            https://github.com/fusion-engineering/rust-git-version
#!RemoteAsset:  sha256:1ad568aa3db0fcbc81f2f116137f263d7304f512a1209b35b85150d3ef88ad19
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(git-version-macro-0.3/default) >= 0.3.9
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "git-version"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
