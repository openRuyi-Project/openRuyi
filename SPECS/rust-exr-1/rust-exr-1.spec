# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name exr
%global full_version 1.74.0
%global pkgname exr-1

Name:           rust-exr-1
Version:        1.74.0
Release:        %autorelease
Summary:        Rust crate "exr"
License:        BSD-3-Clause
URL:            https://github.com/johannesvollmer/exrs
#!RemoteAsset:  sha256:4300e043a56aa2cb633c01af81ca8f699a321879a7854d3896a0ba89056363be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bit-field-0.10/default) >= 0.10.1
Requires:       crate(half-2/default) >= 2.1.0
Requires:       crate(lebe-0.5/default) >= 0.5.2
Requires:       crate(miniz-oxide-0.8/default) >= 0.8.0
Requires:       crate(smallvec-1/default) >= 1.7.0
Requires:       crate(zune-inflate-0.2/zlib) >= 0.2.3
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "exr"

%package     -n %{name}+rayon
Summary:        Read and write OpenEXR files without any unsafe code - feature "rayon" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-core-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust exr crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
