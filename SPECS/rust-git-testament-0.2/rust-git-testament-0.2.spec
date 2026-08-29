# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git-testament
%global full_version 0.2.6
%global pkgname git-testament-0.2

Name:           rust-git-testament-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "git-testament"
License:        BSD-3-Clause
URL:            https://github.com/kinnison/git-testament/
#!RemoteAsset:  sha256:5a74999c921479f919c87a9d2e6922a79a18683f18105344df8e067149232e51
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(git-testament-derive-0.2/default) >= 0.2.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "git-testament"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
