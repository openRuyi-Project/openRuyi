# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name group
%global full_version 0.14.0
%global pkgname group-0.14

Name:           rust-group-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "group"
License:        MIT OR Apache-2.0
URL:            https://github.com/zkcrypto/group
#!RemoteAsset:  sha256:7fd1a1c7a5206c5b7a3f5a0d7ccd3ff85d0c8f5133d62a02680255b0004af5f4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ff-0.14) >= 0.14.0
Requires:       crate(rand-core-0.10) >= 0.10.0
Requires:       crate(subtle-2) >= 2.2.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "group"

%package     -n %{name}+memuse
Summary:        Elliptic curve group traits and utilities - feature "memuse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memuse-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/memuse) = %{version}

%description -n %{name}+memuse
This metapackage enables feature "memuse" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Elliptic curve group traits and utilities - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-xorshift
Summary:        Elliptic curve group traits and utilities - feature "rand_xorshift"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-xorshift-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/rand-xorshift) = %{version}

%description -n %{name}+rand-xorshift
This metapackage enables feature "rand_xorshift" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tests
Summary:        Elliptic curve group traits and utilities - feature "tests"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/rand-xorshift) = %{version}
Provides:       crate(%{pkgname}/tests) = %{version}

%description -n %{name}+tests
This metapackage enables feature "tests" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wnaf-memuse
Summary:        Elliptic curve group traits and utilities - feature "wnaf-memuse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/memuse) = %{version}
Provides:       crate(%{pkgname}/wnaf-memuse) = %{version}

%description -n %{name}+wnaf-memuse
This metapackage enables feature "wnaf-memuse" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
