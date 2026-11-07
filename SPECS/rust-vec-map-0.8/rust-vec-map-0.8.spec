# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vec_map
%global full_version 0.8.2
%global pkgname vec-map-0.8

Name:           rust-vec-map-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "vec_map"
License:        MIT OR Apache-2.0
URL:            https://github.com/contain-rs/vec-map
#!RemoteAsset:  sha256:f1bddf1187be692e79c5ffeab891132dfb0f236ed36a43c7ed39f1165ee20191
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vec_map"

%package     -n %{name}+serde
Summary:        Simple map based on a vector for small integer keys - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/eders) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust vec_map crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "eders" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
