# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustybuzz
%global full_version 0.20.1
%global pkgname rustybuzz-0.20

Name:           rust-rustybuzz-0.20
Version:        0.20.1
Release:        %autorelease
Summary:        Rust crate "rustybuzz"
License:        MIT
URL:            https://github.com/harfbuzz/rustybuzz
#!RemoteAsset:  sha256:fd3c7c96f8a08ee34eff8857b11b49b07d71d1c3f4e88f8a88d4c9e9f90b1702
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.1
Requires:       crate(bytemuck-1/default) >= 1.5.0
Requires:       crate(bytemuck-1/extern-crate-alloc) >= 1.5.0
Requires:       crate(core-maths-0.1/default) >= 0.1.0
Requires:       crate(log-0.4/default) >= 0.4.22
Requires:       crate(smallvec-1/default) >= 1.6.0
Requires:       crate(ttf-parser-0.25/apple-layout) >= 0.25.0
Requires:       crate(ttf-parser-0.25/glyph-names) >= 0.25.0
Requires:       crate(ttf-parser-0.25/no-std-float) >= 0.25.0
Requires:       crate(ttf-parser-0.25/opentype-layout) >= 0.25.0
Requires:       crate(ttf-parser-0.25/variable-fonts) >= 0.25.0
Requires:       crate(unicode-bidi-mirroring-0.4/default) >= 0.4.0
Requires:       crate(unicode-ccc-0.4/default) >= 0.4.0
Requires:       crate(unicode-properties-0.1/general-category) >= 0.1.3
Requires:       crate(unicode-script-0.5/default) >= 0.5.2

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rustybuzz"

%package     -n %{name}+std
Summary:        Complete harfbuzz shaping algorithm port to Rust - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ttf-parser-0.25/apple-layout) >= 0.25.0
Requires:       crate(ttf-parser-0.25/glyph-names) >= 0.25.0
Requires:       crate(ttf-parser-0.25/no-std-float) >= 0.25.0
Requires:       crate(ttf-parser-0.25/opentype-layout) >= 0.25.0
Requires:       crate(ttf-parser-0.25/std) >= 0.25.0
Requires:       crate(ttf-parser-0.25/variable-fonts) >= 0.25.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rustybuzz crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+wasm-shaper
Summary:        Complete harfbuzz shaping algorithm port to Rust - feature "wasm-shaper"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(wasmi-0.37/default) >= 0.37.0
Provides:       crate(%{pkgname}/wasm-shaper) = %{version}

%description -n %{name}+wasm-shaper
This metapackage enables feature "wasm-shaper" for the Rust rustybuzz crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
