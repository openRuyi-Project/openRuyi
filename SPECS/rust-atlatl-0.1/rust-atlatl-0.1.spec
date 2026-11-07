# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atlatl
%global full_version 0.1.2
%global pkgname atlatl-0.1

Name:           rust-atlatl-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "atlatl"
License:        Apache-2.0 OR MIT
URL:            https://github.com/tapeinosyne/atlatl
#!RemoteAsset:  sha256:32bb156841d2e2a888185b5b4f7d93d30efd3a40d1671d9628ab39536adb7ea2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1/default) >= 1.0.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "atlatl"

%package     -n %{name}+serde
Summary:        Double-array tries - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust atlatl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
