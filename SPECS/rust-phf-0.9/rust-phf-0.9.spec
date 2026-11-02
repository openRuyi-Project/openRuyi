# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf
%global full_version 0.9.0
%global pkgname phf-0.9

Name:           rust-phf-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "phf"
License:        MIT
URL:            https://github.com/sfackler/rust-phf
#!RemoteAsset:  sha256:b2ac8b67553a7ca9457ce0e526948cad581819238f4a9d1ea74545851fa24f37
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-shared-0.9) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "phf"

%package     -n %{name}+macros
Summary:        Runtime support for perfect hash function data structures - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/phf-macros) = %{version}
Requires:       crate(%{pkgname}/proc-macro-hack) = %{version}
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phf-macros
Summary:        Runtime support for perfect hash function data structures - feature "phf_macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-macros-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/phf-macros) = %{version}

%description -n %{name}+phf-macros
This metapackage enables feature "phf_macros" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro-hack
Summary:        Runtime support for perfect hash function data structures - feature "proc-macro-hack"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro-hack-0.5/default) >= 0.5.4
Provides:       crate(%{pkgname}/proc-macro-hack) = %{version}

%description -n %{name}+proc-macro-hack
This metapackage enables feature "proc-macro-hack" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Runtime support for perfect hash function data structures - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-shared-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+uncased
Summary:        Runtime support for perfect hash function data structures - feature "uncased"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-shared-0.9/uncased) >= 0.9.0
Provides:       crate(%{pkgname}/uncased) = %{version}

%description -n %{name}+uncased
This metapackage enables feature "uncased" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase
Summary:        Runtime support for perfect hash function data structures - feature "unicase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-shared-0.9/unicase) >= 0.9.0
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust phf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
