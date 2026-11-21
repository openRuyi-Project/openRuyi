# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name timezone_provider
%global full_version 0.2.6
%global pkgname timezone-provider-0.2

Name:           rust-timezone-provider-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "timezone_provider"
License:        MIT OR Apache-2.0
URL:            https://github.com/boa-dev/temporal
#!RemoteAsset:  sha256:89ec4f4eebb4817fde02a411aedc7ac5f66c89c68c49e5d4b17a8139f077af52
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tinystr-0.8/default) >= 0.8.0
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.0
Requires:       crate(zerotrie-0.2/default) >= 0.2.0
Requires:       crate(zerovec-0.11/alloc) >= 0.11.0
Requires:       crate(zerovec-0.11/default) >= 0.11.0
Requires:       crate(zerovec-0.11/derive) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "timezone_provider"

%package     -n %{name}+datagen
Summary:        Time zone data providers - feature "datagen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/experimental-tzif) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(databake-0.2/default) >= 0.2.0
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(serde-1/default) >= 1.0.225
Requires:       crate(serde-1/derive) >= 1.0.225
Requires:       crate(serde-json-1/default) >= 1.0.145
Requires:       crate(tinystr-0.8/databake) >= 0.8.0
Requires:       crate(tinystr-0.8/serde) >= 0.8.0
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.0
Requires:       crate(yoke-0.8/default) >= 0.8.0
Requires:       crate(yoke-0.8/derive) >= 0.8.0
Requires:       crate(zerotrie-0.2/databake) >= 0.2.0
Requires:       crate(zerotrie-0.2/serde) >= 0.2.0
Requires:       crate(zerovec-0.11/alloc) >= 0.11.0
Requires:       crate(zerovec-0.11/databake) >= 0.11.0
Requires:       crate(zerovec-0.11/derive) >= 0.11.0
Requires:       crate(zerovec-0.11/serde) >= 0.11.0
Requires:       crate(zoneinfo-rs-0.1/std) >= 0.1.0
Requires:       crate(zoneinfo-rs-0.1/unstable) >= 0.1.0
Provides:       crate(%{pkgname}/datagen) = %{version}

%description -n %{name}+datagen
This metapackage enables feature "datagen" for the Rust timezone_provider crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental-tzif
Summary:        Time zone data providers - feature "experimental_tzif"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zerofrom-0.1/default) >= 0.1.6
Requires:       crate(zerofrom-0.1/derive) >= 0.1.6
Provides:       crate(%{pkgname}/experimental-tzif) = %{version}

%description -n %{name}+experimental-tzif
This metapackage enables feature "experimental_tzif" for the Rust timezone_provider crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tzif
Summary:        Time zone data providers - feature "tzif"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(combine-4/default) >= 4.6.7
Requires:       crate(jiff-tzdb-0.1/default) >= 0.1.4
Requires:       crate(tzif-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/tzif) = %{version}

%description -n %{name}+tzif
This metapackage enables feature "tzif" for the Rust timezone_provider crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zoneinfo64
Summary:        Time zone data providers - feature "zoneinfo64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zoneinfo64-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/zoneinfo64) = %{version}

%description -n %{name}+zoneinfo64
This metapackage enables feature "zoneinfo64" for the Rust timezone_provider crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
