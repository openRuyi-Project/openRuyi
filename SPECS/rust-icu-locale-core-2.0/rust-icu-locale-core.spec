# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_locale_core
%global full_version 2.2.0
%global pkgname icu-locale-core-2.0

Name:           rust-icu-locale-core-2.0
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "icu_locale_core"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:92219b62b3e2b4d88ac5119f8904c10f8f61bf7e95b640d25ba3075e6cac2c29
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(displaydoc-0.2) >= 0.2.5
Requires:       crate(litemap-0.8) >= 0.8.2
Requires:       crate(tinystr-0.8) >= 0.8.3
Requires:       crate(writeable-0.6) >= 0.6.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "icu_locale_core"

%package     -n %{name}+alloc
Summary:        API for managing Unicode Language and Locale Identifiers - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(litemap-0.8/alloc) >= 0.8.2
Requires:       crate(serde-1.0/alloc) >= 1.0.220
Requires:       crate(tinystr-0.8/alloc) >= 0.8.3
Requires:       crate(writeable-0.6/alloc) >= 0.6.2
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust icu_locale_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+databake
Summary:        API for managing Unicode Language and Locale Identifiers - feature "databake"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(databake-0.2/derive) >= 0.2.0
Provides:       crate(%{pkgname}/databake)

%description -n %{name}+databake
This metapackage enables feature "databake" for the Rust icu_locale_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        API for managing Unicode Language and Locale Identifiers - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.220
Requires:       crate(tinystr-0.8/serde) >= 0.8.3
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust icu_locale_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerovec
Summary:        API for managing Unicode Language and Locale Identifiers - feature "zerovec"
Requires:       crate(%{pkgname})
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.3
Requires:       crate(zerovec-0.11) >= 0.11.6
Provides:       crate(%{pkgname}/zerovec)

%description -n %{name}+zerovec
This metapackage enables feature "zerovec" for the Rust icu_locale_core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
