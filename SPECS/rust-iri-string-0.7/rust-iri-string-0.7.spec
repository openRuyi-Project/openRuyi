# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iri-string
%global full_version 0.7.12
%global pkgname iri-string-0.7

Name:           rust-iri-string-0.7
Version:        0.7.12
Release:        %autorelease
Summary:        Rust crate "iri-string"
License:        MIT OR Apache-2.0
URL:            https://github.com/lo48576/iri-string
#!RemoteAsset:  sha256:25e659a4bb38e810ebc252e53b5814ff908a8c58c2a9ce2fae1bbec24cbf4e20
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "iri-string"

%package     -n %{name}+alloc
Summary:        IRI as string types - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.103
Requires:       crate(serde-1/derive) >= 1.0.103
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust iri-string crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        IRI as string types - feature "memchr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2) >= 2.4.1
Provides:       crate(%{pkgname}/memchr) = %{version}

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust iri-string crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        IRI as string types - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.103
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust iri-string crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        IRI as string types - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(memchr-2/std) >= 2.4.1
Requires:       crate(serde-1/derive) >= 1.0.103
Requires:       crate(serde-1/std) >= 1.0.103
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust iri-string crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
