# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dary_heap
%global full_version 0.3.8
%global pkgname dary-heap-0.3

Name:           rust-dary-heap-0.3
Version:        0.3.8
Release:        %autorelease
Summary:        Rust crate "dary_heap"
License:        MIT OR Apache-2.0
URL:            https://github.com/hanmertens/dary_heap
#!RemoteAsset:  sha256:06d2e3287df1c007e74221c49ca10a95d557349e54b3a75dc2fb14712c751f04
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/extra) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/unstable-nightly) = %{version}

%description
Source code for takopackized Rust crate "dary_heap"

%package     -n %{name}+serde
Summary:        D-ary heap - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust dary_heap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
