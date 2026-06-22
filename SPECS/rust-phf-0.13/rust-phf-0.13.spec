# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf
%global full_version 0.13.1
%global pkgname phf-0.13

Name:           rust-phf-0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Rust crate "phf"
License:        MIT
URL:            https://github.com/rust-phf/rust-phf
#!RemoteAsset:  sha256:c1562dc717473dbaa4c1f85a36410e03c047b2e7df7f45ee938fbef64ae7fadf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-shared-0.13) >= 0.13.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "phf"

%package     -n %{name}+phf-macros
Summary:        Runtime support for perfect hash function data structures - feature "phf_macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-macros-0.13/default) >= 0.13.1
Provides:       crate(%{pkgname}/macros) = %{version}
Provides:       crate(%{pkgname}/phf-macros) = %{version}

%description -n %{name}+phf-macros
This metapackage enables feature "phf_macros" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macros" feature.

%package     -n %{name}+serde
Summary:        Runtime support for perfect hash function data structures - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Runtime support for perfect hash function data structures - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-shared-0.13/std) >= 0.13.1
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+uncased
Summary:        Runtime support for perfect hash function data structures - feature "uncased"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-macros-0.13/uncased) >= 0.13.1
Requires:       crate(phf-shared-0.13/uncased) >= 0.13.1
Provides:       crate(%{pkgname}/uncased) = %{version}

%description -n %{name}+uncased
This metapackage enables feature "uncased" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase
Summary:        Runtime support for perfect hash function data structures - feature "unicase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-macros-0.13/unicase) >= 0.13.1
Requires:       crate(phf-shared-0.13/unicase) >= 0.13.1
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
