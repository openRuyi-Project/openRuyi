# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ttf-parser
%global full_version 0.25.1
%global pkgname ttf-parser-0.25

Name:           rust-ttf-parser-0.25
Version:        0.25.1
Release:        %autorelease
Summary:        Rust crate "ttf-parser"
License:        MIT OR Apache-2.0
URL:            https://github.com/harfbuzz/ttf-parser
#!RemoteAsset:  sha256:d2df906b07856748fa3f6e0ad0cbaa047052d4a7dd609e231c4f72cee8c36f31
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/apple-layout) = %{version}
Provides:       crate(%{pkgname}/glyph-names) = %{version}
Provides:       crate(%{pkgname}/gvar-alloc) = %{version}
Provides:       crate(%{pkgname}/opentype-layout) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/variable-fonts) = %{version}

%description
Source code for takopackized Rust crate "ttf-parser"

%package     -n %{name}+core-maths
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT - feature "core_maths" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-maths-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/core-maths) = %{version}
Provides:       crate(%{pkgname}/no-std-float) = %{version}

%description -n %{name}+core-maths
This metapackage enables feature "core_maths" for the Rust ttf-parser crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "no-std-float" feature.

%package     -n %{name}+default
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/apple-layout) = %{version}
Requires:       crate(%{pkgname}/glyph-names) = %{version}
Requires:       crate(%{pkgname}/opentype-layout) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/variable-fonts) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ttf-parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
