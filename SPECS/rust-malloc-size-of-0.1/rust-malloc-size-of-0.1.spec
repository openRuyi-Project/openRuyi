# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name malloc_size_of
%global full_version 0.1.1
%global pkgname malloc-size-of-0.1

Name:           rust-malloc-size-of-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "malloc_size_of"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/malloc_size_of
#!RemoteAsset:  sha256:e5d719de8b8f230028cf8192ae4c1b25267cd6b8a99d2747d345a70b8c81aa13
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "malloc_size_of"

%package     -n %{name}+void
Summary:        An allocator-agnostic crate for measuring the heap size of a value - feature "void"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(void-1/default) >= 1.0.2
Provides:       crate(%{pkgname}/void) = %{version}

%description -n %{name}+void
This metapackage enables feature "void" for the Rust malloc_size_of crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
