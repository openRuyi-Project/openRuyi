# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dashmap
%global full_version 6.1.0
%global pkgname dashmap-6.0

Name:           rust-dashmap-6.0
Version:        6.1.0
Release:        %autorelease
Summary:        Rust crate "dashmap"
License:        MIT
URL:            https://github.com/xacrimon/dashmap
#!RemoteAsset:  sha256:5041cc499144891f3790297212f32a74fb938e5136a14943f338ef9e0ae276cf
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.21
Requires:       crate(hashbrown-0.14/raw) >= 0.14.5
Requires:       crate(lock-api-0.4/default) >= 0.4.14
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(parking-lot-core-0.9/default) >= 0.9.12
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/raw-api)

%description
Source code for takopackized Rust crate "dashmap"

%package     -n %{name}+arbitrary
Summary:        Blazing fast concurrent HashMap for Rust - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.3.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inline
Summary:        Blazing fast concurrent HashMap for Rust - feature "inline"
Requires:       crate(%{pkgname})
Requires:       crate(hashbrown-0.14/inline-more) >= 0.14.5
Requires:       crate(hashbrown-0.14/raw) >= 0.14.5
Provides:       crate(%{pkgname}/inline)

%description -n %{name}+inline
This metapackage enables feature "inline" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Blazing fast concurrent HashMap for Rust - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.7.0
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Blazing fast concurrent HashMap for Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.188
Requires:       crate(serde-1.0/derive) >= 1.0.188
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+typesize
Summary:        Blazing fast concurrent HashMap for Rust - feature "typesize"
Requires:       crate(%{pkgname})
Requires:       crate(typesize-0.1) >= 0.1.8
Provides:       crate(%{pkgname}/typesize)

%description -n %{name}+typesize
This metapackage enables feature "typesize" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
