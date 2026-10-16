# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-queue
%global full_version 0.3.14
%global pkgname crossbeam-queue-0.3

Name:           rust-crossbeam-queue-0.3
Version:        0.3.14
Release:        %autorelease
Summary:        Rust crate "crossbeam-queue"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-queue
#!RemoteAsset:  sha256:03e8bd762f7479489c70ed6c768ddca99d7296857de437a68dcb2a94365b3fae
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-utils-0.8) >= 0.8.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "crossbeam-queue"

%package     -n %{name}+nightly
Summary:        Concurrent queues - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.8/nightly) >= 0.8.18
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust crossbeam-queue crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Concurrent queues - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(crossbeam-utils-0.8/std) >= 0.8.18
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust crossbeam-queue crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
