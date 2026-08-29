# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytesize
%global full_version 2.4.0
%global pkgname bytesize-2

Name:           rust-bytesize-2
Version:        2.4.0
Release:        %autorelease
Summary:        Rust crate "bytesize"
License:        Apache-2.0
URL:            https://github.com/bytesize-rs/bytesize
#!RemoteAsset:  sha256:49e78e506b9d7633710dab98996f22f95f3d0f488e8f1aa162830556ed9fc14d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "bytesize"

%package     -n %{name}+arbitrary
Summary:        Semantic wrapper for byte count representations - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust bytesize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Semantic wrapper for byte count representations - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bytesize crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
