# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_core
%global full_version 1.0.228
%global pkgname serde-core-1

Name:           rust-serde-core-1
Version:        1.0.228
Release:        %autorelease
Summary:        Rust crate "serde_core"
License:        MIT OR Apache-2.0
URL:            https://serde.rs
#!RemoteAsset:  sha256:41d385c7d4ca58e59fc732af25c3983b67ac852c1a25000afe1175de458b67ad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-derive-1/default) >= 1.0.228
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/rc) = %{version}
Provides:       crate(%{pkgname}/result) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "serde_core"

%package     -n %{name}+default
Summary:        Serde traits only, with no support for derive -- use the `serde` crate instead - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/result) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust serde_core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
