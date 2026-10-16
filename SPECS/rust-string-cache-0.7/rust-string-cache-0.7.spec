# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name string_cache
%global full_version 0.7.5
%global pkgname string-cache-0.7

Name:           rust-string-cache-0.7
Version:        0.7.5
Release:        %autorelease
Summary:        Rust crate "string_cache"
License:        MIT  OR  Apache-2.0
URL:            https://github.com/servo/string-cache
#!RemoteAsset:  sha256:89c058a82f9fd69b1becf8c274f412281038877c553182f1d02eb027045a2d67
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.0.0
Requires:       crate(new-debug-unreachable-1/default) >= 1.0.0
Requires:       crate(phf-shared-0.7/default) >= 0.7.4
Requires:       crate(precomputed-hash-0.1/default) >= 0.1.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(string-cache-codegen-0.4) >= 0.4.0
Requires:       crate(string-cache-shared-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/log-events) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "string_cache"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
