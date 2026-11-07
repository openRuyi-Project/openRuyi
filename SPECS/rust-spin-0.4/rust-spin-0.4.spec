# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name spin
%global full_version 0.4.10
%global pkgname spin-0.4

Name:           rust-spin-0.4
Version:        0.4.10
Release:        %autorelease
Summary:        Rust crate "spin"
License:        MIT
URL:            https://github.com/mvdnes/spin-rs.git
#!RemoteAsset:  sha256:ceac490aa12c567115b40b7b7fceca03a6c9d53d5defea066123debc83c5dc1f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/const-fn) = %{version}
Provides:       crate(%{pkgname}/once) = %{version}

%description
They may contain data, They are usable without `std` and static initializers are available.
Source code for takopackized Rust crate "spin"

%package     -n %{name}+unstable
Summary:        Synchronization primitives based on spinning - feature "unstable" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/const-fn) = %{version}
Requires:       crate(%{pkgname}/once) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
They may contain data, They are usable without `std` and static initializers are available.
This metapackage enables feature "unstable" for the Rust spin crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
