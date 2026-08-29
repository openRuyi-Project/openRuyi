# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libflate
%global full_version 2.3.0
%global pkgname libflate-2

Name:           rust-libflate-2
Version:        2.3.0
Release:        %autorelease
Summary:        Rust crate "libflate"
License:        MIT
URL:            https://github.com/sile/libflate
#!RemoteAsset:  sha256:cd96e993e5f3368b0cb8497dae6c860c22af8ff18388c61c6c0b86c58d86b5df
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(adler32-1) >= 1.0.0
Requires:       crate(crc32fast-1) >= 1.1.1
Requires:       crate(dary-heap-0.3/default) >= 0.3.5
Requires:       crate(libflate-lz77-2) >= 2.3.0
Requires:       crate(no-std-io2-0.9/alloc) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "libflate"

%package     -n %{name}+std
Summary:        DEFLATE algorithm and related formats (ZLIB, GZIP) - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libflate-lz77-2/std) >= 2.3.0
Requires:       crate(no-std-io2-0.9/alloc) >= 0.9.0
Requires:       crate(no-std-io2-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust libflate crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
