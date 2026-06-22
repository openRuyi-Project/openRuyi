# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name debugid
%global full_version 0.8.0
%global pkgname debugid-0.8

Name:           rust-debugid-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "debugid"
License:        Apache-2.0
URL:            https://sentry.io/
#!RemoteAsset:  sha256:bef552e6f588e446098f6ba40d89ac146c8c7b64aade83c051ee00bb5d2bc18d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(uuid-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "debugid"

%package     -n %{name}+serde
Summary:        Common reusable types for implementing the sentry.io protocol - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.85
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust debugid crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
