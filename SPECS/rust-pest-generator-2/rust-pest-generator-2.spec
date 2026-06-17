# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pest_generator
%global full_version 2.8.6
%global pkgname pest-generator-2

Name:           rust-pest-generator-2
Version:        2.8.6
Release:        %autorelease
Summary:        Rust crate "pest_generator"
License:        MIT OR Apache-2.0
URL:            https://pest.rs/
#!RemoteAsset:  sha256:8040c4647b13b210a963c1ed407c1ff4fdfa01c31d6d2a098218702e6664f94f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pest-2) >= 2.8.6
Requires:       crate(pest-meta-2/default) >= 2.8.6
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/export-internal) = %{version}

%description
Source code for takopackized Rust crate "pest_generator"

%package     -n %{name}+grammar-extras
Summary:        Pest code generator - feature "grammar-extras"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-meta-2/grammar-extras) >= 2.8.6
Provides:       crate(%{pkgname}/grammar-extras) = %{version}

%description -n %{name}+grammar-extras
This metapackage enables feature "grammar-extras" for the Rust pest_generator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+not-bootstrap-in-src
Summary:        Pest code generator - feature "not-bootstrap-in-src"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-meta-2/not-bootstrap-in-src) >= 2.8.6
Provides:       crate(%{pkgname}/not-bootstrap-in-src) = %{version}

%description -n %{name}+not-bootstrap-in-src
This metapackage enables feature "not-bootstrap-in-src" for the Rust pest_generator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pest code generator - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pest-2/std) >= 2.8.6
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pest_generator crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
