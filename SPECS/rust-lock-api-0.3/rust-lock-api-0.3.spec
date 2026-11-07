# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lock_api
%global full_version 0.3.4
%global pkgname lock-api-0.3

Name:           rust-lock-api-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "lock_api"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/parking_lot
#!RemoteAsset:  sha256:c4da24a77a3d8a6d4862d95f72e6fdb9c09a643ecdb402d754004a557f2bec75
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(scopeguard-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Compatible with no_std.
Source code for takopackized Rust crate "lock_api"

%package     -n %{name}+owning-ref
Summary:        Wrappers to create fully-featured Mutex and RwLock types - feature "owning_ref"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(owning-ref-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/owning-ref) = %{version}

%description -n %{name}+owning-ref
Compatible with no_std.
This metapackage enables feature "owning_ref" for the Rust lock_api crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Wrappers to create fully-featured Mutex and RwLock types - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.90
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Compatible with no_std.
This metapackage enables feature "serde" for the Rust lock_api crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
