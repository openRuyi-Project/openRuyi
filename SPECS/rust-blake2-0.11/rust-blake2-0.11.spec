# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name blake2
%global full_version 0.11.0
%global pkgname blake2-0.11

Name:           rust-blake2-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "blake2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:5b5d4d889834ee8ecfc0f8426ad30faf7cdcb10f741a8e6d7224d95325479f6f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.11/default) >= 0.11.0
Requires:       crate(digest-0.11/mac) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/reset) = %{version}
Provides:       crate(%{pkgname}/size-opt) = %{version}

%description
Source code for takopackized Rust crate "blake2"

%package     -n %{name}+alloc
Summary:        BLAKE2 hash functions - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/alloc) >= 0.11.0
Requires:       crate(digest-0.11/mac) >= 0.11.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust blake2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+zeroize
Summary:        BLAKE2 hash functions - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/mac) >= 0.11.0
Requires:       crate(digest-0.11/zeroize) >= 0.11.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust blake2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
