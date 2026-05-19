# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pest_generator
%global full_version 2.8.2
%global pkgname pest-generator-2.0

Name:           rust-pest-generator-2.0
Version:        2.8.2
Release:        %autorelease
Summary:        Rust crate "pest_generator"
License:        MIT OR Apache-2.0
URL:            https://pest.rs/
#!RemoteAsset:  sha256:6d4f36811dfe07f7b8573462465d5cb8965fffc2e71ae377a33aecf14c2c9a2f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pest-2.0) >= 2.8.2
Requires:       crate(pest-meta-2.0/default) >= 2.8.2
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/export-internal)

%description
Source code for takopackized Rust crate "pest_generator"

%package     -n %{name}+grammar-extras
Summary:        Pest code generator - feature "grammar-extras"
Requires:       crate(%{pkgname})
Requires:       crate(pest-meta-2.0/grammar-extras) >= 2.8.2
Provides:       crate(%{pkgname}/grammar-extras)

%description -n %{name}+grammar-extras
This metapackage enables feature "grammar-extras" for the Rust pest_generator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+not-bootstrap-in-src
Summary:        Pest code generator - feature "not-bootstrap-in-src"
Requires:       crate(%{pkgname})
Requires:       crate(pest-meta-2.0/not-bootstrap-in-src) >= 2.8.2
Provides:       crate(%{pkgname}/not-bootstrap-in-src)

%description -n %{name}+not-bootstrap-in-src
This metapackage enables feature "not-bootstrap-in-src" for the Rust pest_generator crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pest code generator - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(pest-2.0/std) >= 2.8.2
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pest_generator crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
