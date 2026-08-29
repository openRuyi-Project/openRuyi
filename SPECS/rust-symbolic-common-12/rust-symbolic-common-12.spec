# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symbolic-common
%global full_version 12.18.3
%global pkgname symbolic-common-12

Name:           rust-symbolic-common-12
Version:        12.18.3
Release:        %autorelease
Summary:        Rust crate "symbolic-common"
License:        MIT
URL:            https://github.com/getsentry/symbolic
#!RemoteAsset:  sha256:332615d90111d8eeaf86a84dc9bbe9f65d0d8c5cf11b4caccedc37754eb0dcfd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(debugid-0.8/default) >= 0.8.0
Requires:       crate(memmap2-0.9/default) >= 0.9.0
Requires:       crate(stable-deref-trait-1/default) >= 1.2.0
Requires:       crate(uuid-1/default) >= 1.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "symbolic-common"

%package     -n %{name}+serde
Summary:        Common types and utilities for symbolic, a library to symbolicate and process stack traces from native applications, minidumps or minified JavaScript - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(debugid-0.8/serde) >= 0.8.0
Requires:       crate(serde-1/default) >= 1.0.171
Requires:       crate(serde-1/derive) >= 1.0.171
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust symbolic-common crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
