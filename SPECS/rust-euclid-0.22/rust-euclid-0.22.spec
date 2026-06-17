# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name euclid
%global full_version 0.22.14
%global pkgname euclid-0.22

Name:           rust-euclid-0.22
Version:        0.22.14
Release:        %autorelease
Summary:        Rust crate "euclid"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/euclid
#!RemoteAsset:  sha256:f1a05365e3b1c6d1650318537c7460c6923f1abdd272ad6842baa2b509957a06
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2) >= 0.2.15
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "euclid"

%package     -n %{name}+arbitrary
Summary:        Geometry primitives - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust euclid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Geometry primitives - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.9.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust euclid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Geometry primitives - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/libm) >= 0.2.15
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust euclid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+malloc-size-of
Summary:        Geometry primitives - feature "malloc_size_of"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malloc-size-of-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/malloc-size-of) = %{version}

%description -n %{name}+malloc-size-of
This metapackage enables feature "malloc_size_of" for the Rust euclid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mint
Summary:        Geometry primitives - feature "mint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mint-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}/mint) = %{version}

%description -n %{name}+mint
This metapackage enables feature "mint" for the Rust euclid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Geometry primitives - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/serde-derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust euclid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Geometry primitives - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/std) >= 0.2.15
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust euclid crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
