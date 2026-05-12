# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lock_api
%global full_version 0.4.14
%global pkgname lock-api-0.4

Name:           rust-lock-api-0.4
Version:        0.4.14
Release:        %autorelease
Summary:        Rust crate "lock_api"
License:        MIT OR Apache-2.0
URL:            https://github.com/Amanieu/parking_lot
#!RemoteAsset:  sha256:224399e74b87b5f3557511d98dff8b14089b3dadafcab6bb93eab67d3aace965
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(scopeguard-1.0) >= 1.2.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/arc-lock)
Provides:       crate(%{pkgname}/atomic-usize)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
Compatible with no_std.
Source code for takopackized Rust crate "lock_api"

%package     -n %{name}+owning-ref
Summary:        Wrappers to create fully-featured Mutex and RwLock types - feature "owning_ref"
Requires:       crate(%{pkgname})
Requires:       crate(owning-ref-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/owning-ref)

%description -n %{name}+owning-ref
Compatible with no_std.
This metapackage enables feature "owning_ref" for the Rust lock_api crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Wrappers to create fully-featured Mutex and RwLock types - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.126
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Compatible with no_std.
This metapackage enables feature "serde" for the Rust lock_api crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
