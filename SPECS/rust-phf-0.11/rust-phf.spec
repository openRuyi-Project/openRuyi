# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf
%global full_version 0.11.3
%global pkgname phf-0.11

Name:           rust-phf-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "phf"
License:        MIT
URL:            https://github.com/rust-phf/rust-phf
#!RemoteAsset:  sha256:1fd6780a80ae0c52cc120a26a1a42c1ae51b247a253e4e06113d23d2c2edd078
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-shared-0.11) >= 0.11.3
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "phf"

%package     -n %{name}+phf-macros
Summary:        Runtime support for perfect hash function data structures - feature "phf_macros" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(phf-macros-0.11/default) >= 0.11.3
Provides:       crate(%{pkgname}/macros)
Provides:       crate(%{pkgname}/phf-macros)

%description -n %{name}+phf-macros
This metapackage enables feature "phf_macros" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macros" feature.

%package     -n %{name}+serde
Summary:        Runtime support for perfect hash function data structures - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Runtime support for perfect hash function data structures - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(phf-shared-0.11/std) >= 0.11.3
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+uncased
Summary:        Runtime support for perfect hash function data structures - feature "uncased"
Requires:       crate(%{pkgname})
Requires:       crate(phf-shared-0.11/uncased) >= 0.11.3
Provides:       crate(%{pkgname}/uncased)

%description -n %{name}+uncased
This metapackage enables feature "uncased" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase
Summary:        Runtime support for perfect hash function data structures - feature "unicase"
Requires:       crate(%{pkgname})
Requires:       crate(phf-macros-0.11/unicase) >= 0.11.3
Requires:       crate(phf-shared-0.11/unicase) >= 0.11.3
Provides:       crate(%{pkgname}/unicase)

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
