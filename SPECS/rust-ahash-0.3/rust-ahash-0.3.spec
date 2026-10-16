# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ahash
%global full_version 0.3.8
%global pkgname ahash-0.3

Name:           rust-ahash-0.3
Version:        0.3.8
Release:        %autorelease
Summary:        Rust crate "ahash"
License:        MIT OR Apache-2.0
URL:            https://github.com/tkaitchuck/ahash
#!RemoteAsset:  sha256:e8fd72866655d1904d6b0997d0b07ba561047d070fbe29de039031c641b61217
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ahash"

%package     -n %{name}+const-random
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "const-random" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-random-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/compile-time-rng) = %{version}
Provides:       crate(%{pkgname}/const-random) = %{version}

%description -n %{name}+const-random
This metapackage enables feature "const-random" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compile-time-rng" feature.

%package     -n %{name}+default
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compile-time-rng) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
