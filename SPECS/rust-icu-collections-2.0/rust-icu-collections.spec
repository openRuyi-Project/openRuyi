# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_collections
%global full_version 2.2.0
%global pkgname icu-collections-2.0

Name:           rust-icu-collections-2.0
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "icu_collections"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:2984d1cd16c883d7935b9e07e44071dca8d917fd52ecc02c04d5fa0b5a3f191c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(displaydoc-0.2) >= 0.2.5
Requires:       crate(potential-utf-0.1/zerovec) >= 0.1.5
Requires:       crate(utf8-iter-1.0) >= 1.0.4
Requires:       crate(yoke-0.8/derive) >= 0.8.2
Requires:       crate(zerofrom-0.1/derive) >= 0.1.7
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "icu_collections"

%package     -n %{name}+alloc
Summary:        Collection of API for use in ICU libraries - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.220
Requires:       crate(serde-1.0/derive) >= 1.0.220
Requires:       crate(zerovec-0.11/alloc) >= 0.11.6
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust icu_collections crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+databake
Summary:        Collection of API for use in ICU libraries - feature "databake"
Requires:       crate(%{pkgname})
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(zerovec-0.11/databake) >= 0.11.6
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname}/databake)

%description -n %{name}+databake
This metapackage enables feature "databake" for the Rust icu_collections crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Collection of API for use in ICU libraries - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(potential-utf-0.1/serde) >= 0.1.5
Requires:       crate(potential-utf-0.1/zerovec) >= 0.1.5
Requires:       crate(serde-1.0/derive) >= 1.0.220
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/serde) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust icu_collections crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
