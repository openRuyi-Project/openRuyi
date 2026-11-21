# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_locale
%global full_version 2.2.0
%global pkgname icu-locale-2

Name:           rust-icu-locale-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "icu_locale"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:d5a396343c7208121dc86e35623d3dfe19814a7613cfd14964994cdc9c9a2e26
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(icu-collections-2) >= 2.2.0
Requires:       crate(icu-locale-core-2/alloc) >= 2.2.0
Requires:       crate(icu-locale-core-2/zerovec) >= 2.2.0
Requires:       crate(icu-provider-2/alloc) >= 2.2.0
Requires:       crate(potential-utf-0.1/alloc) >= 0.1.3
Requires:       crate(potential-utf-0.1/zerovec) >= 0.1.3
Requires:       crate(tinystr-0.8/alloc) >= 0.8.3
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.3
Requires:       crate(zerovec-0.11/alloc) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "icu_locale"

%package     -n %{name}+compiled-data
Summary:        API for Unicode Language and Locale Identifiers canonicalization - feature "compiled_data" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-locale-data-2) >= 2.2.0
Requires:       crate(icu-provider-2/alloc) >= 2.2.0
Requires:       crate(icu-provider-2/baked) >= 2.2.0
Provides:       crate(%{pkgname}/compiled-data) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+compiled-data
This metapackage enables feature "compiled_data" for the Rust icu_locale crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+datagen
Summary:        API for Unicode Language and Locale Identifiers canonicalization - feature "datagen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(icu-collections-2/databake) >= 2.2.0
Requires:       crate(icu-locale-core-2/alloc) >= 2.2.0
Requires:       crate(icu-locale-core-2/databake) >= 2.2.0
Requires:       crate(icu-locale-core-2/zerovec) >= 2.2.0
Requires:       crate(icu-provider-2/alloc) >= 2.2.0
Requires:       crate(icu-provider-2/export) >= 2.2.0
Requires:       crate(tinystr-0.8/alloc) >= 0.8.3
Requires:       crate(tinystr-0.8/databake) >= 0.8.3
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.3
Requires:       crate(zerovec-0.11/alloc) >= 0.11.6
Requires:       crate(zerovec-0.11/databake) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname}/datagen) = %{version}

%description -n %{name}+datagen
This metapackage enables feature "datagen" for the Rust icu_locale crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        API for Unicode Language and Locale Identifiers canonicalization - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-collections-2/serde) >= 2.2.0
Requires:       crate(icu-locale-core-2/alloc) >= 2.2.0
Requires:       crate(icu-locale-core-2/serde) >= 2.2.0
Requires:       crate(icu-locale-core-2/zerovec) >= 2.2.0
Requires:       crate(icu-provider-2/alloc) >= 2.2.0
Requires:       crate(icu-provider-2/serde) >= 2.2.0
Requires:       crate(potential-utf-0.1/alloc) >= 0.1.3
Requires:       crate(potential-utf-0.1/serde) >= 0.1.3
Requires:       crate(potential-utf-0.1/zerovec) >= 0.1.3
Requires:       crate(serde-1/alloc) >= 1.0.220
Requires:       crate(serde-1/derive) >= 1.0.220
Requires:       crate(tinystr-0.8/alloc) >= 0.8.3
Requires:       crate(tinystr-0.8/serde) >= 0.8.3
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.3
Requires:       crate(zerovec-0.11/alloc) >= 0.11.6
Requires:       crate(zerovec-0.11/serde) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust icu_locale crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
