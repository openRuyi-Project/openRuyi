# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name validator
%global full_version 0.19.0
%global pkgname validator-0.19

Name:           rust-validator-0.19
Version:        0.19.0
Release:        %autorelease
Summary:        Rust crate "validator"
License:        MIT
URL:            https://github.com/Keats/validator
#!RemoteAsset:  sha256:d0b4a29d8709210980a09379f27ee31549b73292c87ab9899beee1c0d3be6303
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(idna-1/default) >= 1.0.0
Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(regex-1/std) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(url-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "validator"

%package     -n %{name}+card-validate
Summary:        Common validation functions (email, url, length, ...) and trait - to be used with `validator_derive` - feature "card-validate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(card-validate-2/default) >= 2.3.0
Provides:       crate(%{pkgname}/card) = %{version}
Provides:       crate(%{pkgname}/card-validate) = %{version}

%description -n %{name}+card-validate
This metapackage enables feature "card-validate" for the Rust validator crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "card" feature.

%package     -n %{name}+derive-nightly-features
Summary:        Common validation functions (email, url, length, ...) and trait - to be used with `validator_derive` - feature "derive_nightly_features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(validator-derive-0.19/nightly-features) >= 0.19.0
Provides:       crate(%{pkgname}/derive-nightly-features) = %{version}

%description -n %{name}+derive-nightly-features
This metapackage enables feature "derive_nightly_features" for the Rust validator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Common validation functions (email, url, length, ...) and trait - to be used with `validator_derive` - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(indexmap-2/serde) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust validator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unic-ucd-common
Summary:        Common validation functions (email, url, length, ...) and trait - to be used with `validator_derive` - feature "unic-ucd-common" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unic-ucd-common-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/unic) = %{version}
Provides:       crate(%{pkgname}/unic-ucd-common) = %{version}

%description -n %{name}+unic-ucd-common
This metapackage enables feature "unic-ucd-common" for the Rust validator crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unic" feature.

%package     -n %{name}+validator-derive
Summary:        Common validation functions (email, url, length, ...) and trait - to be used with `validator_derive` - feature "validator_derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(validator-derive-0.19/default) >= 0.19.0
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/validator-derive) = %{version}

%description -n %{name}+validator-derive
This metapackage enables feature "validator_derive" for the Rust validator crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
