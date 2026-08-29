# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name camino
%global full_version 1.2.2
%global pkgname camino-1

Name:           rust-camino-1
Version:        1.2.2
Release:        %autorelease
Summary:        Rust crate "camino"
License:        MIT OR Apache-2.0
URL:            https://github.com/camino-rs/camino
#!RemoteAsset:  sha256:e629a66d692cb9ff1a1c664e41771b3dcaf961985a9774c0eb0bd1b51cf60a48
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "camino"

%package     -n %{name}+proptest1
Summary:        UTF-8 paths - feature "proptest1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proptest-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/proptest1) = %{version}

%description -n %{name}+proptest1
This metapackage enables feature "proptest1" for the Rust camino crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        UTF-8 paths - feature "serde1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust camino crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
