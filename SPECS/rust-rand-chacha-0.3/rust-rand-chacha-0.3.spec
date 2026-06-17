# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_chacha
%global full_version 0.3.1
%global pkgname rand-chacha-0.3

Name:           rust-rand-chacha-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "rand_chacha"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:e6c10a63a0fa32252be49d21e7709d4d4baf8d231c2dbce1eaa8141b9b127d88
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ppv-lite86-0.2/simd) >= 0.2.8
Requires:       crate(rand-core-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}

%description
Source code for takopackized Rust crate "rand_chacha"

%package     -n %{name}+serde
Summary:        ChaCha random number generator - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand_chacha crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde1" feature.

%package     -n %{name}+std
Summary:        ChaCha random number generator - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ppv-lite86-0.2/simd) >= 0.2.8
Requires:       crate(ppv-lite86-0.2/std) >= 0.2.8
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand_chacha crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
