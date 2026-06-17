# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerofrom
%global full_version 0.1.7
%global pkgname zerofrom-0.1

Name:           rust-zerofrom-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "zerofrom"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:69faa1f2a1ea75661980b013019ed6687ed0e83d069bc1114e2cc74c6c04c4df
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zerofrom"

%package     -n %{name}+derive
Summary:        ZeroFrom trait for constructing - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zerofrom-derive-0.1) >= 0.1.6
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust zerofrom crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
