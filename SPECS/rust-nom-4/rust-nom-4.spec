# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nom
%global full_version 4.2.3
%global pkgname nom-4

Name:           rust-nom-4
Version:        4.2.3
Release:        %autorelease
Summary:        Rust crate "nom"
License:        MIT
URL:            https://github.com/Geal/nom
#!RemoteAsset:  sha256:2ad2a91a8e869eeb30b9cb3119ae87773a8f4ae617f41b1eb9c154b2905f7bd6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2) >= 2.0.0
Requires:       crate(version-check-0.1) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/verbose-errors) = %{version}

%description
Source code for takopackized Rust crate "nom"

%package     -n %{name}+lazy-static
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "lazy_static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lazy-static-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/lazy-static) = %{version}

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust nom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "regex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/regex) = %{version}
Provides:       crate(%{pkgname}/regexp) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust nom crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "regexp" feature.

%package     -n %{name}+regexp-macros
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "regexp_macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lazy-static) = %{version}
Requires:       crate(%{pkgname}/regexp) = %{version}
Provides:       crate(%{pkgname}/regexp-macros) = %{version}

%description -n %{name}+regexp-macros
This metapackage enables feature "regexp_macros" for the Rust nom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(memchr-2/use-std) >= 2.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust nom crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
