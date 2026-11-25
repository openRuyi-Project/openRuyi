# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ctutils
%global full_version 0.4.8
%global pkgname ctutils-0.4

Name:           rust-ctutils-0.4
Version:        0.4.8
Release:        %autorelease
Summary:        Rust crate "ctutils"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:261af4dc7a06ea8a527a8717d8cbba3417530d6ea14e1edb3de6b67806be474f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cmov-0.5/default) >= 0.5.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Supports `const fn` where appropriate. Built on the `cmov` crate which provides architecture-specific predication intrinsics. Heavily inspired by the `subtle` crate.
Source code for takopackized Rust crate "ctutils"

%package     -n %{name}+subtle
Summary:        Constant-time utility library with selection and equality testing support targeting cryptographic applications - feature "subtle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(subtle-2) >= 2.6.0
Provides:       crate(%{pkgname}/subtle) = %{version}

%description -n %{name}+subtle
Supports `const fn` where appropriate. Built on the `cmov` crate which provides architecture-specific predication intrinsics. Heavily inspired by the `subtle` crate.
This metapackage enables feature "subtle" for the Rust ctutils crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
