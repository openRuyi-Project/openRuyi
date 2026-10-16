# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name alloc-stdlib
%global full_version 0.2.4
%global pkgname alloc-stdlib-0.2

Name:           rust-alloc-stdlib-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "alloc-stdlib"
License:        BSD-3-Clause
URL:            https://github.com/dropbox/rust-alloc-no-stdlib
#!RemoteAsset:  sha256:0e76a019e91224d279006ff972f1e984179a6e9feb050adba6ce8274aef23195
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(alloc-no-stdlib-2/default) >= 2.0.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "alloc-stdlib"

%package     -n %{name}+unsafe
Summary:        Dynamic allocator example that may be used with the stdlib - feature "unsafe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(alloc-no-stdlib-2/unsafe) >= 2.0.4
Provides:       crate(%{pkgname}/unsafe) = %{version}

%description -n %{name}+unsafe
This metapackage enables feature "unsafe" for the Rust alloc-stdlib crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
