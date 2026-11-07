# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-queue
%global full_version 0.2.3
%global pkgname crossbeam-queue-0.2

Name:           rust-crossbeam-queue-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "crossbeam-queue"
License:        MIT OR Apache-2.0 AND BSD-2-Clause
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils
#!RemoteAsset:  sha256:774ba60a54c213d409d5353bda12d49cd68d14e45036a285234c8d6f91f92570
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-0.1/default) >= 0.1.2
Requires:       crate(crossbeam-utils-0.7) >= 0.7.0
Requires:       crate(maybe-uninit-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "crossbeam-queue"

%package     -n %{name}+alloc
Summary:        Concurrent queues - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.7/alloc) >= 0.7.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust crossbeam-queue crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Concurrent queues - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.7/std) >= 0.7.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust crossbeam-queue crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
