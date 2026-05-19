# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pest_meta
%global full_version 2.8.2
%global pkgname pest-meta-2.0

Name:           rust-pest-meta-2.0
Version:        2.8.2
Release:        %autorelease
Summary:        Rust crate "pest_meta"
License:        MIT OR Apache-2.0
URL:            https://pest.rs/
#!RemoteAsset:  sha256:42919b05089acbd0a5dcd5405fb304d17d1053847b81163d09c4ad18ce8e8420
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pest-2.0/default) >= 2.8.2
Requires:       crate(sha2-0.10) >= 0.10.9
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/grammar-extras)

%description
Source code for takopackized Rust crate "pest_meta"

%package     -n %{name}+not-bootstrap-in-src
Summary:        Pest meta language parser and validator - feature "not-bootstrap-in-src"
Requires:       crate(%{pkgname})
Requires:       crate(cargo-0.81/default) >= 0.81.0
Provides:       crate(%{pkgname}/not-bootstrap-in-src)

%description -n %{name}+not-bootstrap-in-src
This metapackage enables feature "not-bootstrap-in-src" for the Rust pest_meta crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
