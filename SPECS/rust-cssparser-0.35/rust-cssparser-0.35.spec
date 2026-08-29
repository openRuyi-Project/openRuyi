# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cssparser
%global full_version 0.35.0
%global pkgname cssparser-0.35

Name:           rust-cssparser-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "cssparser"
License:        MPL-2.0
URL:            https://github.com/servo/rust-cssparser
#!RemoteAsset:  sha256:4e901edd733a1472f944a45116df3f846f54d37e67e68640ac8bb69689aca2aa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cssparser-macros-0.6/default) >= 0.6.1
Requires:       crate(dtoa-short-0.3/default) >= 0.3.0
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(phf-0.11/default) >= 0.11.2
Requires:       crate(phf-0.11/macros) >= 0.11.2
Requires:       crate(smallvec-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dummy-match-byte) = %{version}
Provides:       crate(%{pkgname}/skip-long-tests) = %{version}

%description
Source code for takopackized Rust crate "cssparser"

%package     -n %{name}+malloc-size-of
Summary:        CSS Syntax Level 3 - feature "malloc_size_of"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malloc-size-of-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/malloc-size-of) = %{version}

%description -n %{name}+malloc-size-of
This metapackage enables feature "malloc_size_of" for the Rust cssparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        CSS Syntax Level 3 - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust cssparser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
