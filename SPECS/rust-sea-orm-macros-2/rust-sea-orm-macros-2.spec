# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sea-orm-macros
%global full_version 2.0.0
%global pkgname sea-orm-macros-2

Name:           rust-sea-orm-macros-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "sea-orm-macros"
License:        MIT OR Apache-2.0
URL:            https://www.sea-ql.org/SeaORM
#!RemoteAsset:  sha256:b4cbb7ae053b9b37c919ea944a3bc52f7830a90c223f8a765c908293bca8f22d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5) >= 0.5.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(pluralizer-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1) >= 1.0.0
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(syn-2/derive) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Requires:       crate(syn-2/proc-macro) >= 2.0.0
Requires:       crate(unicode-ident-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/entity-registry) = %{version}
Provides:       crate(%{pkgname}/postgres-array) = %{version}
Provides:       crate(%{pkgname}/sqlx-postgres) = %{version}
Provides:       crate(%{pkgname}/strum) = %{version}
Provides:       crate(%{pkgname}/with-arrow) = %{version}
Provides:       crate(%{pkgname}/with-json) = %{version}

%description
Source code for takopackized Rust crate "sea-orm-macros"

%package     -n %{name}+bae
Summary:        Derive macros for SeaORM - feature "bae" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sea-bae-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/bae) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+bae
This metapackage enables feature "bae" for the Rust sea-orm-macros crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "derive" features.

%package     -n %{name}+proc-macro-crate
Summary:        Derive macros for SeaORM - feature "proc-macro-crate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro-crate-3/default) >= 3.2.0
Provides:       crate(%{pkgname}/proc-macro-crate) = %{version}
Provides:       crate(%{pkgname}/seaography) = %{version}

%description -n %{name}+proc-macro-crate
This metapackage enables feature "proc-macro-crate" for the Rust sea-orm-macros crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "seaography" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
