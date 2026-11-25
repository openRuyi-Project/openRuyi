# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lock_free_hashtable
%global full_version 0.1.4
%global pkgname lock-free-hashtable-0.1

Name:           rust-lock-free-hashtable-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "lock_free_hashtable"
License:        MIT OR Apache-2.0
URL:            https://github.com/facebook/buck2
#!RemoteAsset:  sha256:ebf3631712f5b790675292ff827af269f5d9f920c920b77dc41d0485e3719612
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atomic-0.5/default) >= 0.5.3
Requires:       crate(parking-lot-0.12/default) >= 0.12.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lock_free_hashtable"

%package     -n %{name}+allocative
Summary:        Lock-free (almost) insertion only hashtable - feature "allocative"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(allocative-0.3) >= 0.3.6
Provides:       crate(%{pkgname}/allocative) = %{version}

%description -n %{name}+allocative
This metapackage enables feature "allocative" for the Rust lock_free_hashtable crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
