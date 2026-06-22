# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-test
%global full_version 0.2.6
%global pkgname tracing-test-0.2

Name:           rust-tracing-test-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "tracing-test"
License:        MIT
URL:            https://github.com/dbrgn/tracing-test
#!RemoteAsset:  sha256:19a4c448db514d4f24c5ddb9f73f2ee71bfb24c526cf0c570ba142d1119e0051
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tracing-core-0.1/default) >= 0.1.0
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.0
Requires:       crate(tracing-test-macro-0.2/default) >= 0.2.6
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tracing-test"

%package     -n %{name}+no-env-filter
Summary:        Helper functions and macros that allow for easier testing of crates that use `tracing` - feature "no-env-filter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-test-macro-0.2/no-env-filter) >= 0.2.6
Provides:       crate(%{pkgname}/no-env-filter) = %{version}

%description -n %{name}+no-env-filter
This metapackage enables feature "no-env-filter" for the Rust tracing-test crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
