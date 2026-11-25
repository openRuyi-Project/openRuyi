# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dashmap
%global full_version 7.0.0-rc2
%global pkgname dashmap-7.0.0-rc2

Name:           rust-dashmap-7.0.0-rc2
Version:        7.0.0
Release:        %autorelease
Summary:        Rust crate "dashmap"
License:        MIT
URL:            https://github.com/xacrimon/dashmap
#!RemoteAsset:  sha256:e4a1e35a65fe0538a60167f0ada6e195ad5d477f6ddae273943596d4a1a5730b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.0
Requires:       crate(equivalent-1/default) >= 1.0.1
Requires:       crate(hashbrown-0.15) >= 0.15.2
Requires:       crate(lock-api-0.4/default) >= 0.4.12
Requires:       crate(parking-lot-core-0.9/default) >= 0.9.10

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/raw-api) = %{version}

%description
Source code for takopackized Rust crate "dashmap"

%package     -n %{name}+all
Summary:        Blazing fast concurrent HashMap for Rust - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arbitrary) = %{version}
Requires:       crate(%{pkgname}/raw-api) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/typesize) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arbitrary
Summary:        Blazing fast concurrent HashMap for Rust - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.4.1
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inline-more
Summary:        Blazing fast concurrent HashMap for Rust - feature "inline-more"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.15/inline-more) >= 0.15.2
Provides:       crate(%{pkgname}/inline-more) = %{version}

%description -n %{name}+inline-more
This metapackage enables feature "inline-more" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Blazing fast concurrent HashMap for Rust - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Blazing fast concurrent HashMap for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.217
Requires:       crate(serde-1/derive) >= 1.0.217
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+typesize
Summary:        Blazing fast concurrent HashMap for Rust - feature "typesize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(typesize-0.1/hashbrown-15) >= 0.1.13
Provides:       crate(%{pkgname}/typesize) = %{version}

%description -n %{name}+typesize
This metapackage enables feature "typesize" for the Rust dashmap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
