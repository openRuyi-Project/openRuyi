# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name scc
%global full_version 2.4.0
%global pkgname scc-2

Name:           rust-scc-2
Version:        2.4.0
Release:        %autorelease
Summary:        Rust crate "scc"
License:        Apache-2.0
URL:            https://github.com/wvwwvwwv/scalable-concurrent-containers/
#!RemoteAsset:  sha256:46e6f046b7fef48e2660c57ed794263155d713de679057f2d0c169bfc6e756cc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(sdd-3/default) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "scc"

%package     -n %{name}+equivalent
Summary:        High-performance containers and utilities for concurrent and asynchronous programming - feature "equivalent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(equivalent-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/equivalent) = %{version}

%description -n %{name}+equivalent
This metapackage enables feature "equivalent" for the Rust scc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loom
Summary:        High-performance containers and utilities for concurrent and asynchronous programming - feature "loom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(loom-0.7/default) >= 0.7.0
Requires:       crate(sdd-3/loom) >= 3.0.0
Provides:       crate(%{pkgname}/loom) = %{version}

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust scc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        High-performance containers and utilities for concurrent and asynchronous programming - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust scc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
