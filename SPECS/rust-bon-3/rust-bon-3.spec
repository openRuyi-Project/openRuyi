# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bon
%global full_version 3.9.0
%global pkgname bon-3

Name:           rust-bon-3
Version:        3.9.0
Release:        %autorelease
Summary:        Rust crate "bon"
License:        MIT OR Apache-2.0
URL:            https://bon-rs.com
#!RemoteAsset:  sha256:2d13a61f2963b88eef9c1be03df65d42f6996dfeac1054870d950fcf66686f83
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bon-macros-3/default) >= 3.9.0
Requires:       crate(rustversion-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/experimental-getter) = %{version}

%description
Source code for takopackized Rust crate "bon"

%package     -n %{name}+alloc
Summary:        Next-gen compile-time-checked builder generator, named function's arguments, and more! - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bon-macros-3/alloc) >= 3.9.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental-generics-setters
Summary:        Next-gen compile-time-checked builder generator, named function's arguments, and more! - feature "experimental-generics-setters"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bon-macros-3/experimental-generics-setters) >= 3.9.0
Provides:       crate(%{pkgname}/experimental-generics-setters) = %{version}

%description -n %{name}+experimental-generics-setters
This metapackage enables feature "experimental-generics-setters" for the Rust bon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental-overwritable
Summary:        Next-gen compile-time-checked builder generator, named function's arguments, and more! - feature "experimental-overwritable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bon-macros-3/experimental-overwritable) >= 3.9.0
Provides:       crate(%{pkgname}/experimental-overwritable) = %{version}

%description -n %{name}+experimental-overwritable
This metapackage enables feature "experimental-overwritable" for the Rust bon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+implied-bounds
Summary:        Next-gen compile-time-checked builder generator, named function's arguments, and more! - feature "implied-bounds"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bon-macros-3/implied-bounds) >= 3.9.0
Provides:       crate(%{pkgname}/implied-bounds) = %{version}

%description -n %{name}+implied-bounds
This metapackage enables feature "implied-bounds" for the Rust bon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Next-gen compile-time-checked builder generator, named function's arguments, and more! - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bon-macros-3/std) >= 3.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bon crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
