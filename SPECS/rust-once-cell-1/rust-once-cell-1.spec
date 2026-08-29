# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name once_cell
%global full_version 1.21.4
%global pkgname once-cell-1

Name:           rust-once-cell-1
Version:        1.21.4
Release:        %autorelease
Summary:        Rust crate "once_cell"
License:        MIT OR Apache-2.0
URL:            https://github.com/matklad/once_cell
#!RemoteAsset:  sha256:9f7c3e4beb33f85d45ae3e3a1792185706c8e16d043238c593331cc7cd313b50
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/race) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "once_cell"

%package     -n %{name}+critical-section
Summary:        Single assignment cells and lazy values - feature "critical-section" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/portable-atomic) = %{version}
Requires:       crate(critical-section-1/default) >= 1.1.3
Provides:       crate(%{pkgname}/atomic-polyfill) = %{version}
Provides:       crate(%{pkgname}/critical-section) = %{version}

%description -n %{name}+critical-section
This metapackage enables feature "critical-section" for the Rust once_cell crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "atomic-polyfill" feature.

%package     -n %{name}+parking-lot
Summary:        Single assignment cells and lazy values - feature "parking_lot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-core-0.9) >= 0.9.10
Provides:       crate(%{pkgname}/parking-lot) = %{version}

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust once_cell crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Single assignment cells and lazy values - feature "portable-atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1) >= 1.8.0
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust once_cell crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
