# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cedarwood
%global full_version 0.4.6
%global pkgname cedarwood-0.4

Name:           rust-cedarwood-0.4
Version:        0.4.6
Release:        %autorelease
Summary:        Rust crate "cedarwood"
License:        BSD-2-Clause
URL:            https://github.com/MnO2/cedarwood
#!RemoteAsset:  sha256:6d910bedd62c24733263d0bed247460853c9d22e8956bd4cd964302095e04e90
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(smallvec-1/default) >= 1.6.1
Requires:       crate(smallvec-1/union) >= 1.6.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/reduced-trie) = %{version}

%description
Source code for takopackized Rust crate "cedarwood"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
