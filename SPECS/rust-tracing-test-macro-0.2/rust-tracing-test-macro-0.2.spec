# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-test-macro
%global full_version 0.2.6
%global pkgname tracing-test-macro-0.2

Name:           rust-tracing-test-macro-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "tracing-test-macro"
License:        MIT
URL:            https://github.com/dbrgn/tracing-test
#!RemoteAsset:  sha256:ad06847b7afb65c7866a36664b75c40b895e318cea4f71299f013fb22965329d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-env-filter) = %{version}

%description
Internal crate, should only be used through the `tracing-test` crate.
Source code for takopackized Rust crate "tracing-test-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
