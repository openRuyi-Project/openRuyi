# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_normalizer
%global full_version 2.2.0
%global pkgname icu-normalizer-2

Name:           rust-icu-normalizer-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "icu_normalizer"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:c56e5ee99d6e3d33bd91c5d85458b6005a22140021cc324cea84dd0e72cff3b4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(icu-collections-2) >= 2.2.0
Requires:       crate(icu-provider-2) >= 2.2.0
Requires:       crate(smallvec-1) >= 1.10.0
Requires:       crate(zerovec-0.11) >= 0.11.6
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/write16) = %{version}

%description
Source code for takopackized Rust crate "icu_normalizer"

%package     -n %{name}+compiled-data
Summary:        API for normalizing text into Unicode Normalization Forms - feature "compiled_data"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-normalizer-data-2) >= 2.2.0
Requires:       crate(icu-properties-2/compiled-data) >= 2.2.0
Requires:       crate(icu-provider-2/baked) >= 2.2.0
Provides:       crate(%{pkgname}/compiled-data) = %{version}

%description -n %{name}+compiled-data
This metapackage enables feature "compiled_data" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+datagen
Summary:        API for normalizing text into Unicode Normalization Forms - feature "datagen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/icu-properties) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(icu-collections-2/databake) >= 2.2.0
Requires:       crate(icu-properties-2/datagen) >= 2.2.0
Requires:       crate(icu-provider-2/export) >= 2.2.0
Requires:       crate(zerovec-0.11/databake) >= 0.11.6
Provides:       crate(%{pkgname}/datagen) = %{version}

%description -n %{name}+datagen
This metapackage enables feature "datagen" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        API for normalizing text into Unicode Normalization Forms - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compiled-data) = %{version}
Requires:       crate(%{pkgname}/utf16-iter) = %{version}
Requires:       crate(%{pkgname}/utf8-iter) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+harfbuzz-traits
Summary:        API for normalizing text into Unicode Normalization Forms - feature "harfbuzz_traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(harfbuzz-traits-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/harfbuzz-traits) = %{version}

%description -n %{name}+harfbuzz-traits
This metapackage enables feature "harfbuzz_traits" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+icu-properties
Summary:        API for normalizing text into Unicode Normalization Forms - feature "icu_properties"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-properties-2) >= 2.2.0
Provides:       crate(%{pkgname}/icu-properties) = %{version}

%description -n %{name}+icu-properties
This metapackage enables feature "icu_properties" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        API for normalizing text into Unicode Normalization Forms - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-collections-2/serde) >= 2.2.0
Requires:       crate(icu-properties-2/serde) >= 2.2.0
Requires:       crate(icu-provider-2/serde) >= 2.2.0
Requires:       crate(serde-1/alloc) >= 1.0.220
Requires:       crate(serde-1/derive) >= 1.0.220
Requires:       crate(zerovec-0.11/serde) >= 0.11.6
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+utf16-iter
Summary:        API for normalizing text into Unicode Normalization Forms - feature "utf16_iter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(utf16-iter-1) >= 1.0.2
Requires:       crate(write16-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/utf16-iter) = %{version}

%description -n %{name}+utf16-iter
This metapackage enables feature "utf16_iter" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+utf8-iter
Summary:        API for normalizing text into Unicode Normalization Forms - feature "utf8_iter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(utf8-iter-1) >= 1.0.2
Provides:       crate(%{pkgname}/utf8-iter) = %{version}

%description -n %{name}+utf8-iter
This metapackage enables feature "utf8_iter" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
