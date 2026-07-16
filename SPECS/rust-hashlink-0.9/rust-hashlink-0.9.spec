# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hashlink
%global full_version 0.9.1
%global pkgname hashlink-0.9

Name:           rust-hashlink-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "hashlink"
License:        MIT OR Apache-2.0
URL:            https://github.com/kyren/hashlink
#!RemoteAsset:  sha256:6ba4ff7128dee98c7dc9794b6a411377e1404dba1c97deb8d1a55297bd25d8af
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.14/ahash) >= 0.14.3
Requires:       crate(hashbrown-0.14/inline-more) >= 0.14.3

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
