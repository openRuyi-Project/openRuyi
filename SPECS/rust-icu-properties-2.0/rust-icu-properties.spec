# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_properties
%global full_version 2.2.0
%global pkgname icu-properties-2.0

Name:           rust-icu-properties-2.0
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "icu_properties"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:bee3b67d0ea5c2cca5003417989af8996f8604e34fb9ddf96208a033901e70de
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(icu-collections-2.0) >= 2.2.0
Requires:       crate(icu-locale-core-2.0/zerovec) >= 2.2.0
Requires:       crate(icu-provider-2.0) >= 2.2.0
Requires:       crate(zerotrie-0.2/yoke) >= 0.2.4
Requires:       crate(zerotrie-0.2/zerofrom) >= 0.2.4
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "icu_properties"

%package     -n %{name}+alloc
Summary:        Definitions for Unicode properties - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(icu-collections-2.0/alloc) >= 2.2.0
Requires:       crate(serde-1.0/alloc) >= 1.0.220
Requires:       crate(serde-1.0/derive) >= 1.0.220
Requires:       crate(zerovec-0.11/alloc) >= 0.11.6
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust icu_properties crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compiled-data
Summary:        Definitions for Unicode properties - feature "compiled_data" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(icu-properties-data-2.0) >= 2.2.0
Requires:       crate(icu-provider-2.0/baked) >= 2.2.0
Provides:       crate(%{pkgname}/compiled-data)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+compiled-data
This metapackage enables feature "compiled_data" for the Rust icu_properties crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+datagen
Summary:        Definitions for Unicode properties - feature "datagen"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(icu-collections-2.0/databake) >= 2.2.0
Requires:       crate(icu-locale-core-2.0/databake) >= 2.2.0
Requires:       crate(icu-locale-core-2.0/zerovec) >= 2.2.0
Requires:       crate(icu-provider-2.0/export) >= 2.2.0
Requires:       crate(zerotrie-0.2/databake) >= 0.2.4
Requires:       crate(zerotrie-0.2/yoke) >= 0.2.4
Requires:       crate(zerotrie-0.2/zerofrom) >= 0.2.4
Requires:       crate(zerovec-0.11/databake) >= 0.11.6
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname}/datagen)

%description -n %{name}+datagen
This metapackage enables feature "datagen" for the Rust icu_properties crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+harfbuzz-traits
Summary:        Definitions for Unicode properties - feature "harfbuzz_traits"
Requires:       crate(%{pkgname})
Requires:       crate(harfbuzz-traits-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/harfbuzz-traits)

%description -n %{name}+harfbuzz-traits
This metapackage enables feature "harfbuzz_traits" for the Rust icu_properties crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Definitions for Unicode properties - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(icu-collections-2.0/serde) >= 2.2.0
Requires:       crate(icu-locale-core-2.0/serde) >= 2.2.0
Requires:       crate(icu-locale-core-2.0/zerovec) >= 2.2.0
Requires:       crate(icu-provider-2.0/serde) >= 2.2.0
Requires:       crate(serde-1.0/derive) >= 1.0.220
Requires:       crate(zerotrie-0.2/serde) >= 0.2.4
Requires:       crate(zerotrie-0.2/yoke) >= 0.2.4
Requires:       crate(zerotrie-0.2/zerofrom) >= 0.2.4
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/serde) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust icu_properties crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-bidi
Summary:        Definitions for Unicode properties - feature "unicode_bidi"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-bidi-0.3) >= 0.3.11
Provides:       crate(%{pkgname}/unicode-bidi)

%description -n %{name}+unicode-bidi
This metapackage enables feature "unicode_bidi" for the Rust icu_properties crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
