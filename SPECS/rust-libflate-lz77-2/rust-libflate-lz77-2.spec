# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libflate_lz77
%global full_version 2.3.0
%global pkgname libflate-lz77-2

Name:           rust-libflate-lz77-2
Version:        2.3.0
Release:        %autorelease
Summary:        Rust crate "libflate_lz77"
License:        MIT
URL:            https://github.com/sile/libflate
#!RemoteAsset:  sha256:ff7a10e427698aef6eef269482776debfef63384d30f13aad39a1a95e0e098fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.16/default) >= 0.16.0
Requires:       crate(no-std-io2-0.9/alloc) >= 0.9.0
Requires:       crate(rle-decode-fast-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "libflate_lz77"

%package     -n %{name}+std
Summary:        LZ77 encoder for libflate crate - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(no-std-io2-0.9/alloc) >= 0.9.0
Requires:       crate(no-std-io2-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust libflate_lz77 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
