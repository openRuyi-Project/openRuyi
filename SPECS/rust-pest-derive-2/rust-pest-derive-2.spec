# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pest_derive
%global full_version 2.8.6
%global pkgname pest-derive-2

Name:           rust-pest-derive-2
Version:        2.8.6
Release:        %autorelease
Summary:        Rust crate "pest_derive"
License:        MIT OR Apache-2.0
URL:            https://pest.rs/
#!RemoteAsset:  sha256:11f486f1ea21e6c10ed15d5a7c77165d0ee443402f0780849d1768e7d9d6fe77
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pest-2) >= 2.8.6
Requires:       crate(pest-generator-2) >= 2.8.6
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pest_derive"

%package     -n %{name}+grammar-extras
Summary:        Pest's derive macro - feature "grammar-extras"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-generator-2/grammar-extras) >= 2.8.6
Provides:       crate(%{pkgname}/grammar-extras) = %{version}

%description -n %{name}+grammar-extras
This metapackage enables feature "grammar-extras" for the Rust pest_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+not-bootstrap-in-src
Summary:        Pest's derive macro - feature "not-bootstrap-in-src"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-generator-2/not-bootstrap-in-src) >= 2.8.6
Provides:       crate(%{pkgname}/not-bootstrap-in-src) = %{version}

%description -n %{name}+not-bootstrap-in-src
This metapackage enables feature "not-bootstrap-in-src" for the Rust pest_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pest's derive macro - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-2/std) >= 2.8.6
Requires:       crate(pest-generator-2/std) >= 2.8.6
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pest_derive crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
