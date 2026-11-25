# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name byte-unit
%global full_version 5.2.0
%global pkgname byte-unit-5

Name:           rust-byte-unit-5
Version:        5.2.0
Release:        %autorelease
Summary:        Rust crate "byte-unit"
License:        MIT
URL:            https://magiclen.org/byte-unit
#!RemoteAsset:  sha256:8c6d47a4e2961fb8721bcfc54feae6455f2f64e7054f9bc67e875f0e77f4c58d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(utf8-width-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/u128) = %{version}

%description
Source code for takopackized Rust crate "byte-unit"

%package     -n %{name}+default
Summary:        Interacting with units of bytes - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/byte) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust byte-unit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rocket
Summary:        Interacting with units of bytes - feature "rocket"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(rocket-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/rocket) = %{version}

%description -n %{name}+rocket
This metapackage enables feature "rocket" for the Rust byte-unit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        Interacting with units of bytes - feature "rust_decimal" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1) >= 1.0.0
Provides:       crate(%{pkgname}/bit) = %{version}
Provides:       crate(%{pkgname}/byte) = %{version}
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
This metapackage enables feature "rust_decimal" for the Rust byte-unit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bit", and "byte" features.

%package     -n %{name}+schemars
Summary:        Interacting with units of bytes - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-1) >= 1.0.0
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust byte-unit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Interacting with units of bytes - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust byte-unit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Interacting with units of bytes - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1/std) >= 1.0.0
Requires:       crate(schemars-1/std) >= 1.0.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust byte-unit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
