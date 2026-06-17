# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name miniz_oxide
%global full_version 0.8.9
%global pkgname miniz-oxide-0.8

Name:           rust-miniz-oxide-0.8
Version:        0.8.9
Release:        %autorelease
Summary:        Rust crate "miniz_oxide"
License:        MIT OR Zlib OR Apache-2.0
URL:            https://github.com/Frommi/miniz_oxide/tree/master/miniz_oxide
#!RemoteAsset:  sha256:1fa76a2c86f704bdb222d66965fb3d63269ce38518b83cb0575fca855ebb6316
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(adler2-2) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/block-boundary) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/with-alloc) = %{version}

%description
Source code for takopackized Rust crate "miniz_oxide"

%package     -n %{name}+rustc-dep-of-std
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(adler2-2/rustc-dep-of-std) >= 2.0.0
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust miniz_oxide crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust miniz_oxide crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd-adler32
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz - feature "simd-adler32" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simd-adler32-0.3) >= 0.3.3
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/simd-adler32) = %{version}

%description -n %{name}+simd-adler32
This metapackage enables feature "simd-adler32" for the Rust miniz_oxide crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "simd" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
