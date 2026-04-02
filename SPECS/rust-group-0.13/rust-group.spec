# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name group
%global full_version 0.13.0
%global pkgname group-0.13

Name:           rust-group-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "group"
License:        MIT/Apache-2.0
URL:            https://github.com/zkcrypto/group
#!RemoteAsset:  sha256:f0f9ef7462f7c099f518d754361858f86d8a07af53ba9af0fe635bbccb151a63
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ff-0.13) >= 0.13.1
Requires:       crate(rand-core-0.6) >= 0.6.4
Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "group"

%package     -n %{name}+memuse
Summary:        Elliptic curve group traits and utilities - feature "memuse"
Requires:       crate(%{pkgname})
Requires:       crate(memuse-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/memuse)

%description -n %{name}+memuse
This metapackage enables feature "memuse" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Elliptic curve group traits and utilities - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-xorshift
Summary:        Elliptic curve group traits and utilities - feature "rand_xorshift"
Requires:       crate(%{pkgname})
Requires:       crate(rand-xorshift-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/rand-xorshift)

%description -n %{name}+rand-xorshift
This metapackage enables feature "rand_xorshift" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tests
Summary:        Elliptic curve group traits and utilities - feature "tests"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/rand)
Requires:       crate(%{pkgname}/rand-xorshift)
Provides:       crate(%{pkgname}/tests)

%description -n %{name}+tests
This metapackage enables feature "tests" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wnaf-memuse
Summary:        Elliptic curve group traits and utilities - feature "wnaf-memuse"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/memuse)
Provides:       crate(%{pkgname}/wnaf-memuse)

%description -n %{name}+wnaf-memuse
This metapackage enables feature "wnaf-memuse" for the Rust group crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
