# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hashbrown
%global full_version 0.1.8
%global pkgname hashbrown-0.1

Name:           rust-hashbrown-0.1
Version:        0.1.8
Release:        %autorelease
Summary:        Rust crate "hashbrown"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/hashbrown
#!RemoteAsset:  sha256:3bae29b6653b3412c2e71e9d486db9f9df5d701941d86683005efb9f2d28e3da
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1) >= 1.0.0
Requires:       crate(scopeguard-0.3) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "hashbrown"

%package     -n %{name}+rayon
Summary:        Rust port of Google's SwissTable hash map - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Rust port of Google's SwissTable hash map - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
