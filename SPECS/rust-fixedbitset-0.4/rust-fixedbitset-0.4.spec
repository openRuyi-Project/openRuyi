# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fixedbitset
%global full_version 0.4.2
%global pkgname fixedbitset-0.4

Name:           rust-fixedbitset-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "fixedbitset"
License:        MIT OR Apache-2.0
URL:            https://github.com/petgraph/fixedbitset
#!RemoteAsset:  sha256:0ce7134b9999ecaf8bcd65542e436736ef32ddca1b3e06094cb6ec5755203b80
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "fixedbitset"

%package     -n %{name}+serde
Summary:        Simple bitset collection - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust fixedbitset crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
