# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name expect-test
%global full_version 1.5.0
%global pkgname expect-test-1

Name:           rust-expect-test-1
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "expect-test"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-analyzer/expect-test
#!RemoteAsset:  sha256:9e0be0a561335815e06dab7c62e50353134c796e7a6155402a64bcff66b6a5e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dissimilar-1/default) >= 1.0.0
Requires:       crate(once-cell-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "expect-test"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
