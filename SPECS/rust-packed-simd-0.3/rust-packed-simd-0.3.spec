# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name packed_simd
%global full_version 0.3.9
%global pkgname packed-simd-0.3

Name:           rust-packed-simd-0.3
Version:        0.3.9
Release:        %autorelease
Summary:        Rust crate "packed_simd"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/packed_simd
#!RemoteAsset:  sha256:1f9f08af0c877571712e2e3e686ad79efad9657dbf0f7c3c8ba943ff6c38932d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(num-traits-0.2/libm) >= 0.2.14

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/into-bits) = %{version}
Provides:       crate(%{pkgname}/libcore-neon) = %{version}

%description
Source code for takopackized Rust crate "packed_simd"

%package     -n %{name}+core-arch
Summary:        Portable Packed SIMD vectors - feature "core_arch"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-arch-0.1/default) >= 0.1.5
Provides:       crate(%{pkgname}/core-arch) = %{version}

%description -n %{name}+core-arch
This metapackage enables feature "core_arch" for the Rust packed_simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sleef-sys
Summary:        Portable Packed SIMD vectors - feature "sleef-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sleef-sys-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/sleef-sys) = %{version}

%description -n %{name}+sleef-sys
This metapackage enables feature "sleef-sys" for the Rust packed_simd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
