# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name priority-queue
%global full_version 2.7.0
%global pkgname priority-queue-2

Name:           rust-priority-queue-2
Version:        2.7.0
Release:        %autorelease
Summary:        Rust crate "priority-queue"
License:        LGPL-3.0-or-later OR MPL-2.0
URL:            https://github.com/garro95/priority-queue
#!RemoteAsset:  sha256:93980406f12d9f8140ed5abe7155acb10bb1e69ea55c88960b9c2f117445ef96
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(equivalent-1/default) >= 1.0.1
Requires:       crate(indexmap-2) >= 2.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/benchmarks) = %{version}

%description
Source code for takopackized Rust crate "priority-queue"

%package     -n %{name}+serde
Summary:        Priority Queue implemented as a heap with a function to efficiently change the priority of an item - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust priority-queue crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Priority Queue implemented as a heap with a function to efficiently change the priority of an item - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/std) >= 2.2.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust priority-queue crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
