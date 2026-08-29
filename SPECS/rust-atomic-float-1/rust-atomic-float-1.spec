# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atomic_float
%global full_version 1.1.0
%global pkgname atomic-float-1

Name:           rust-atomic-float-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "atomic_float"
License:        Apache-2.0 OR MIT OR Unlicense
URL:            https://github.com/thomcc/atomic_float
#!RemoteAsset:  sha256:628d228f918ac3b82fe590352cc719d30664a0c13ca3a60266fe02c7132d480a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/atomic-f64) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "atomic_float"

%package     -n %{name}+serde
Summary:        Floating point types which can be safely shared between threads - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust atomic_float crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
