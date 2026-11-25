# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sea-orm-arrow
%global full_version 2.0.0-rc.3
%global pkgname sea-orm-arrow-2.0.0-rc.3

Name:           rust-sea-orm-arrow-2.0.0-rc.3
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "sea-orm-arrow"
License:        MIT OR Apache-2.0
URL:            https://www.sea-ql.org/SeaORM
#!RemoteAsset:  sha256:5c2eee8405f16c1f337fe3a83389361caea83c928d14dbd666a480407072c365
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
Patch2000:      2000-select-system-sea-query.patch
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-57) >= 57.0.0
Requires:       crate(sea-query-1/thread-safe) = 1.0.1
Requires:       crate(thiserror-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sea-orm-arrow"

%package     -n %{name}+prettyprint
Summary:        Arrow integration for SeaORM - feature "prettyprint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-57/prettyprint) >= 57.0.0
Provides:       crate(%{pkgname}/prettyprint) = %{version}

%description -n %{name}+prettyprint
This metapackage enables feature "prettyprint" for the Rust sea-orm-arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-bigdecimal
Summary:        Arrow integration for SeaORM - feature "with-bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) = 1.0.1
Requires:       crate(sea-query-1/with-bigdecimal) = 1.0.1
Provides:       crate(%{pkgname}/with-bigdecimal) = %{version}

%description -n %{name}+with-bigdecimal
This metapackage enables feature "with-bigdecimal" for the Rust sea-orm-arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-chrono
Summary:        Arrow integration for SeaORM - feature "with-chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) = 1.0.1
Requires:       crate(sea-query-1/with-chrono) = 1.0.1
Provides:       crate(%{pkgname}/with-chrono) = %{version}

%description -n %{name}+with-chrono
This metapackage enables feature "with-chrono" for the Rust sea-orm-arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-rust-decimal
Summary:        Arrow integration for SeaORM - feature "with-rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) = 1.0.1
Requires:       crate(sea-query-1/with-rust-decimal) = 1.0.1
Provides:       crate(%{pkgname}/with-rust-decimal) = %{version}

%description -n %{name}+with-rust-decimal
This metapackage enables feature "with-rust_decimal" for the Rust sea-orm-arrow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-time
Summary:        Arrow integration for SeaORM - feature "with-time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-query-1/thread-safe) = 1.0.1
Requires:       crate(sea-query-1/with-time) = 1.0.1
Provides:       crate(%{pkgname}/with-time) = %{version}

%description -n %{name}+with-time
This metapackage enables feature "with-time" for the Rust sea-orm-arrow crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
