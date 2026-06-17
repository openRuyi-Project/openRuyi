# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name allocator-api2
%global full_version 0.2.21
%global pkgname allocator-api2-0.2

Name:           rust-allocator-api2-0.2
Version:        0.2.21
Release:        %autorelease
Summary:        Rust crate "allocator-api2"
License:        MIT OR Apache-2.0
URL:            https://github.com/zakarumych/allocator-api2
#!RemoteAsset:  sha256:683d7910e743518b0e34f1186f92494becacb047c7b6bf616c96772180fef923
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fresh-rust) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "allocator-api2"

%package     -n %{name}+serde
Summary:        Mirror of Rust's allocator API - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust allocator-api2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
