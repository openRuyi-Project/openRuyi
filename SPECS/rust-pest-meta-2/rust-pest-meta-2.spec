# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pest_meta
%global full_version 2.8.6
%global pkgname pest-meta-2

Name:           rust-pest-meta-2
Version:        2.8.6
Release:        %autorelease
Summary:        Rust crate "pest_meta"
License:        MIT OR Apache-2.0
URL:            https://pest.rs/
#!RemoteAsset:  sha256:89815c69d36021a140146f26659a81d6c2afa33d216d736dd4be5381a7362220
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pest-2/default) >= 2.8.6
Requires:       crate(sha2-0.10) >= 0.10.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/grammar-extras) = %{version}

%description
Source code for takopackized Rust crate "pest_meta"

%package     -n %{name}+not-bootstrap-in-src
Summary:        Pest meta language parser and validator - feature "not-bootstrap-in-src"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cargo-0.81/default) >= 0.81.0
Provides:       crate(%{pkgname}/not-bootstrap-in-src) = %{version}

%description -n %{name}+not-bootstrap-in-src
This metapackage enables feature "not-bootstrap-in-src" for the Rust pest_meta crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
