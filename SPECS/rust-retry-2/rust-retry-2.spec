# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name retry
%global full_version 2.2.0
%global pkgname retry-2

Name:           rust-retry-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "retry"
License:        MIT
URL:            https://github.com/jimmycuadra/retry
#!RemoteAsset:  sha256:1cab9bd343c737660e523ee69f788018f3db686d537d2fd0f99c9f747c1bda4f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "retry"

%package     -n %{name}+rand
Summary:        Utilities for retrying operations that can fail - feature "rand" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/random) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust retry crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "random" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
