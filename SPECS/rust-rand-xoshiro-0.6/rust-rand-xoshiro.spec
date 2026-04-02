# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_xoshiro
%global full_version 0.6.0
%global pkgname rand-xoshiro-0.6

Name:           rust-rand-xoshiro-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "rand_xoshiro"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:6f97cdb2a36ed4183de61b2f824cc45c9f1037f28afe0a322e9fff4c108b5aaa
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.6/default) >= 0.6.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "rand_xoshiro"

%package     -n %{name}+serde
Summary:        Xoshiro, xoroshiro and splitmix64 random number generators - feature "serde" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/serde1)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand_xoshiro crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde1" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
