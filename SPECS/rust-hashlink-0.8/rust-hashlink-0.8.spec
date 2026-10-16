# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hashlink
%global full_version 0.8.4
%global pkgname hashlink-0.8

Name:           rust-hashlink-0.8
Version:        0.8.4
Release:        %autorelease
Summary:        Rust crate "hashlink"
License:        MIT OR Apache-2.0
URL:            https://github.com/kyren/hashlink
#!RemoteAsset:  sha256:e8094feaf31ff591f651a2664fb9cfd92bba7a60ce3197265e9482ebe753c8f7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.14/default) >= 0.14.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hashlink"

%package     -n %{name}+serde
Summary:        HashMap-like containers that hold their key-value pairs in a user controllable order - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-impl) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust hashlink crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde_impl" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
