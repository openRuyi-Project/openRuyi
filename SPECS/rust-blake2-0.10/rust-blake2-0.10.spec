# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name blake2
%global full_version 0.10.6
%global pkgname blake2-0.10

Name:           rust-blake2-0.10
Version:        0.10.6
Release:        %autorelease
Summary:        Rust crate "blake2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:46502ad458c9a52b69d4d4d32775c788b7a1b85e8bc9d482d92250fc0e3f8efe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.10/default) >= 0.10.3
Requires:       crate(digest-0.10/mac) >= 0.10.3
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/reset) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/simd-asm) = %{version}
Provides:       crate(%{pkgname}/simd-opt) = %{version}
Provides:       crate(%{pkgname}/size-opt) = %{version}

%description
Source code for takopackized Rust crate "blake2"

%package     -n %{name}+std
Summary:        BLAKE2 hash functions - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/mac) >= 0.10.3
Requires:       crate(digest-0.10/std) >= 0.10.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust blake2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
