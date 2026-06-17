# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name either
%global full_version 1.16.0
%global pkgname either-1

Name:           rust-either-1
Version:        1.16.0
Release:        %autorelease
Summary:        Rust crate "either"
License:        MIT OR Apache-2.0
URL:            https://github.com/rayon-rs/either
#!RemoteAsset:  sha256:91622ff5e7162018101f2fea40d6ebf4a78bbe5a49736a2020649edf9693679e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description
Source code for takopackized Rust crate "either"

%package     -n %{name}+serde
Summary:        Enum `Either` with variants `Left` and `Right` is a general purpose sum type with two cases - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.95
Requires:       crate(serde-1/derive) >= 1.0.95
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust either crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
