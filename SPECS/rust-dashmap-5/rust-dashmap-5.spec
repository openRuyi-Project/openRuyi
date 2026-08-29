# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dashmap
%global full_version 5.5.3
%global pkgname dashmap-5

Name:           rust-dashmap-5
Version:        5.5.3
Release:        %autorelease
Summary:        Rust crate "dashmap"
License:        MIT
URL:            https://github.com/xacrimon/dashmap
#!RemoteAsset:  sha256:978747c1d849a7d2ee5e8adc0159961c48fb7e5db2f06af6723b80123bb53856
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(hashbrown-0.14) >= 0.14.0
Requires:       crate(lock-api-0.4/default) >= 0.4.10
Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(parking-lot-core-0.9/default) >= 0.9.8
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/raw-api) = %{version}

%description
Source code for takopackized Rust crate "dashmap"

%package     -n %{name}+arbitrary
Summary:        Blazing fast concurrent HashMap for Rust - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inline
Summary:        Blazing fast concurrent HashMap for Rust - feature "inline"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.14/inline-more) >= 0.14.0
Provides:       crate(%{pkgname}/inline) = %{version}

%description -n %{name}+inline
This metapackage enables feature "inline" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Blazing fast concurrent HashMap for Rust - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.7.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Blazing fast concurrent HashMap for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.188
Requires:       crate(serde-1/derive) >= 1.0.188
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
