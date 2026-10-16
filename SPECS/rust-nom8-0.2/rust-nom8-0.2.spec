# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nom8
%global full_version 0.2.0
%global pkgname nom8-0.2

Name:           rust-nom8-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "nom8"
License:        MIT
URL:            https://github.com/epage/nom-experimental
#!RemoteAsset:  sha256:ae01545c9c7fc4486ab7debaf2aad7003ac19431791868fb2e8066df97fad2f8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2) >= 2.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "nom8"

%package     -n %{name}+std
Summary:        Byte-oriented, zero-copy, parser combinators library (fork for proposals for v8) - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(memchr-2/std) >= 2.3.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust nom8 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+unstable-doc
Summary:        Byte-oriented, zero-copy, parser combinators library (fork for proposals for v8) - feature "unstable-doc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-doc) = %{version}

%description -n %{name}+unstable-doc
This metapackage enables feature "unstable-doc" for the Rust nom8 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
