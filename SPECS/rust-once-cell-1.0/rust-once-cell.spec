# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name once_cell
%global full_version 1.21.4
%global pkgname once-cell-1.0

Name:           rust-once-cell-1.0
Version:        1.21.4
Release:        %autorelease
Summary:        Rust crate "once_cell"
License:        MIT OR Apache-2.0
URL:            https://github.com/matklad/once_cell
#!RemoteAsset:  sha256:9f7c3e4beb33f85d45ae3e3a1792185706c8e16d043238c593331cc7cd313b50
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/race)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "once_cell"

%package     -n %{name}+critical-section
Summary:        Single assignment cells and lazy values - feature "critical-section" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/portable-atomic)
Requires:       crate(critical-section-1.0/default) >= 1.1.3
Provides:       crate(%{pkgname}/atomic-polyfill)
Provides:       crate(%{pkgname}/critical-section)

%description -n %{name}+critical-section
This metapackage enables feature "critical-section" for the Rust once_cell crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "atomic-polyfill" feature.

%package     -n %{name}+parking-lot
Summary:        Single assignment cells and lazy values - feature "parking_lot"
Requires:       crate(%{pkgname})
Requires:       crate(parking-lot-core-0.9) >= 0.9.10
Provides:       crate(%{pkgname}/parking-lot)

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust once_cell crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Single assignment cells and lazy values - feature "portable-atomic"
Requires:       crate(%{pkgname})
Requires:       crate(portable-atomic-1.0) >= 1.8
Provides:       crate(%{pkgname}/portable-atomic)

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust once_cell crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
