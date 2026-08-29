# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cedarwood
%global full_version 0.5.0
%global pkgname cedarwood-0.5

Name:           rust-cedarwood-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "cedarwood"
License:        BSD-2-Clause
URL:            https://github.com/MnO2/cedarwood
#!RemoteAsset:  sha256:c0524a528a6a0288df1863c3c20fe92c301875b4941e7b6c4b394ab08c5a4c55
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(smallvec-1/default) >= 1.13.0
Requires:       crate(smallvec-1/union) >= 1.13.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/reduced-trie) = %{version}

%description
Source code for takopackized Rust crate "cedarwood"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
