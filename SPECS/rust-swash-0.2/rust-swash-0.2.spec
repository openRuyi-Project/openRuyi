# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name swash
%global full_version 0.2.9
%global pkgname swash-0.2

Name:           rust-swash-0.2
Version:        0.2.9
Release:        %autorelease
Summary:        Rust crate "swash"
License:        Apache-2.0 OR MIT
URL:            https://github.com/dfrg/swash
#!RemoteAsset:  sha256:0811b01ca2c4e8718760713911feaf4675c24f94e50530a015ec646cfb622f7c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(skrifa-0.31) >= 0.31.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "swash"

%package     -n %{name}+default
Summary:        Font introspection, complex text shaping and glyph rendering - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/render) = %{version}
Requires:       crate(%{pkgname}/scale) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust swash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Font introspection, complex text shaping and glyph rendering - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-maths-0.1/default) >= 0.1.1
Requires:       crate(skrifa-0.31/libm) >= 0.31.1
Requires:       crate(zeno-0.3/libm) >= 0.3.3
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust swash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+render
Summary:        Font introspection, complex text shaping and glyph rendering - feature "render"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/scale) = %{version}
Requires:       crate(zeno-0.3/eval) >= 0.3.3
Provides:       crate(%{pkgname}/render) = %{version}

%description -n %{name}+render
This metapackage enables feature "render" for the Rust swash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scale
Summary:        Font introspection, complex text shaping and glyph rendering - feature "scale"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(yazi-0.2) >= 0.2.1
Requires:       crate(zeno-0.3) >= 0.3.3
Provides:       crate(%{pkgname}/scale) = %{version}

%description -n %{name}+scale
This metapackage enables feature "scale" for the Rust swash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Font introspection, complex text shaping and glyph rendering - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(skrifa-0.31/std) >= 0.31.1
Requires:       crate(yazi-0.2/std) >= 0.2.1
Requires:       crate(zeno-0.3/std) >= 0.3.3
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust swash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
