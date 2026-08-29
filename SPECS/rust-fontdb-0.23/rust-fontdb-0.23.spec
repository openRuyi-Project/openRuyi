# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fontdb
%global full_version 0.23.0
%global pkgname fontdb-0.23

Name:           rust-fontdb-0.23
Version:        0.23.0
Release:        %autorelease
Summary:        Rust crate "fontdb"
License:        MIT
URL:            https://github.com/RazrFalcon/fontdb
#!RemoteAsset:  sha256:457e789b3d1202543297a350643cf459f836cade38934e7a4cf6a39e7cde2905
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(slotmap-1) >= 1.0.6
Requires:       crate(tinyvec-1/alloc) >= 1.6.0
Requires:       crate(tinyvec-1/default) >= 1.6.0
Requires:       crate(ttf-parser-0.25/apple-layout) >= 0.25.0
Requires:       crate(ttf-parser-0.25/glyph-names) >= 0.25.0
Requires:       crate(ttf-parser-0.25/no-std-float) >= 0.25.0
Requires:       crate(ttf-parser-0.25/opentype-layout) >= 0.25.0
Requires:       crate(ttf-parser-0.25/variable-fonts) >= 0.25.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "fontdb"

%package     -n %{name}+default
Summary:        Simple, in-memory font database with CSS-like queries - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fontconfig) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/memmap) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust fontdb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fontconfig
Summary:        Simple, in-memory font database with CSS-like queries - feature "fontconfig"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fontconfig-parser) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Provides:       crate(%{pkgname}/fontconfig) = %{version}

%description -n %{name}+fontconfig
This metapackage enables feature "fontconfig" for the Rust fontdb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fontconfig-parser
Summary:        Simple, in-memory font database with CSS-like queries - feature "fontconfig-parser"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fontconfig-parser-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/fontconfig-parser) = %{version}

%description -n %{name}+fontconfig-parser
This metapackage enables feature "fontconfig-parser" for the Rust fontdb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memmap
Summary:        Simple, in-memory font database with CSS-like queries - feature "memmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/memmap2) = %{version}
Provides:       crate(%{pkgname}/memmap) = %{version}

%description -n %{name}+memmap
This metapackage enables feature "memmap" for the Rust fontdb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memmap2
Summary:        Simple, in-memory font database with CSS-like queries - feature "memmap2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memmap2-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/memmap2) = %{version}

%description -n %{name}+memmap2
This metapackage enables feature "memmap2" for the Rust fontdb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Simple, in-memory font database with CSS-like queries - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ttf-parser-0.25/apple-layout) >= 0.25.0
Requires:       crate(ttf-parser-0.25/glyph-names) >= 0.25.0
Requires:       crate(ttf-parser-0.25/no-std-float) >= 0.25.0
Requires:       crate(ttf-parser-0.25/opentype-layout) >= 0.25.0
Requires:       crate(ttf-parser-0.25/std) >= 0.25.0
Requires:       crate(ttf-parser-0.25/variable-fonts) >= 0.25.0
Provides:       crate(%{pkgname}/fs) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust fontdb crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fs" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
