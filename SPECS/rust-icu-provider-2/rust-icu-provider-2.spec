# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_provider
%global full_version 2.2.0
%global pkgname icu-provider-2

Name:           rust-icu-provider-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "icu_provider"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:139c4cf31c8b5f33d7e199446eff9c1e02decfc2f0eec2c8d71f65befa45b421
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(displaydoc-0.2) >= 0.2.3
Requires:       crate(icu-locale-core-2) >= 2.2.0
Requires:       crate(yoke-0.8/derive) >= 0.8.2
Requires:       crate(zerofrom-0.1/derive) >= 0.1.6
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}
Provides:       crate(%{pkgname}/zerotrie) = %{version}

%description
Source code for takopackized Rust crate "icu_provider"

%package     -n %{name}+alloc
Summary:        Trait and struct definitions for the ICU data provider - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-locale-core-2/alloc) >= 2.2.0
Requires:       crate(serde-1/alloc) >= 1.0.220
Requires:       crate(serde-1/derive) >= 1.0.220
Requires:       crate(stable-deref-trait-1) >= 1.2.0
Requires:       crate(writeable-0.6) >= 0.6.1
Requires:       crate(yoke-0.8/alloc) >= 0.8.2
Requires:       crate(yoke-0.8/derive) >= 0.8.2
Requires:       crate(zerofrom-0.1/alloc) >= 0.1.6
Requires:       crate(zerofrom-0.1/derive) >= 0.1.6
Requires:       crate(zerotrie-0.2/alloc) >= 0.2.4
Requires:       crate(zerovec-0.11/alloc) >= 0.11.6
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust icu_provider crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+baked
Summary:        Trait and struct definitions for the ICU data provider - feature "baked"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(writeable-0.6) >= 0.6.1
Requires:       crate(zerotrie-0.2) >= 0.2.4
Provides:       crate(%{pkgname}/baked) = %{version}

%description -n %{name}+baked
This metapackage enables feature "baked" for the Rust icu_provider crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deserialize-bincode-1
Summary:        Trait and struct definitions for the ICU data provider - feature "deserialize_bincode_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(bincode-1/default) >= 1.3.1
Provides:       crate(%{pkgname}/deserialize-bincode-1) = %{version}

%description -n %{name}+deserialize-bincode-1
This metapackage enables feature "deserialize_bincode_1" for the Rust icu_provider crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deserialize-json
Summary:        Trait and struct definitions for the ICU data provider - feature "deserialize_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.45
Provides:       crate(%{pkgname}/deserialize-json) = %{version}

%description -n %{name}+deserialize-json
This metapackage enables feature "deserialize_json" for the Rust icu_provider crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deserialize-postcard-1
Summary:        Trait and struct definitions for the ICU data provider - feature "deserialize_postcard_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(postcard-1) >= 1.0.3
Provides:       crate(%{pkgname}/deserialize-postcard-1) = %{version}

%description -n %{name}+deserialize-postcard-1
This metapackage enables feature "deserialize_postcard_1" for the Rust icu_provider crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+export
Summary:        Trait and struct definitions for the ICU data provider - feature "export"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(erased-serde-0.4/default) >= 0.4.0
Requires:       crate(postcard-1) >= 1.0.3
Requires:       crate(zerovec-0.11/databake) >= 0.11.6
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Provides:       crate(%{pkgname}/export) = %{version}

%description -n %{name}+export
This metapackage enables feature "export" for the Rust icu_provider crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Trait and struct definitions for the ICU data provider - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4) >= 0.4.17
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust icu_provider crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Trait and struct definitions for the ICU data provider - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.220
Requires:       crate(yoke-0.8/derive) >= 0.8.2
Requires:       crate(yoke-0.8/serde) >= 0.8.2
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust icu_provider crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
