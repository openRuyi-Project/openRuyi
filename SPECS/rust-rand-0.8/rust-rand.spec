# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand
%global full_version 0.8.5
%global pkgname rand-0.8

Name:           rust-rand-0.8
Version:        0.8.5
Release:        %autorelease
Summary:        Rust crate "rand"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:34af8d1a0e25924bc5b7c43c079c942339d8f0a8b57c39049bef581b46327404
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.6/default) >= 0.6.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/min-const-gen)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/small-rng)

%description
Source code for takopackized Rust crate "rand"

%package     -n %{name}+alloc
Summary:        Random number generators and other randomness functionality - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6/alloc) >= 0.6.4
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Random number generators and other randomness functionality - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/std-rng)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Random number generators and other randomness functionality - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6/getrandom) >= 0.6.4
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Random number generators and other randomness functionality - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.186
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Random number generators and other randomness functionality - feature "log"
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+packed-simd
Summary:        Random number generators and other randomness functionality - feature "packed_simd" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(packed-simd-2-0.3/default) >= 0.3.7
Requires:       crate(packed-simd-2-0.3/into-bits) >= 0.3.7
Provides:       crate(%{pkgname}/packed-simd)
Provides:       crate(%{pkgname}/simd-support)

%description -n %{name}+packed-simd
This metapackage enables feature "packed_simd" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "simd_support" feature.

%package     -n %{name}+rand-chacha
Summary:        Random number generators and other randomness functionality - feature "rand_chacha" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rand-chacha-0.3) >= 0.3.1
Provides:       crate(%{pkgname}/rand-chacha)
Provides:       crate(%{pkgname}/std-rng)

%description -n %{name}+rand-chacha
This metapackage enables feature "rand_chacha" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std_rng" feature.

%package     -n %{name}+serde
Summary:        Random number generators and other randomness functionality - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.103
Requires:       crate(serde-1.0/derive) >= 1.0.103
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        Random number generators and other randomness functionality - feature "serde1"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(rand-core-0.6/serde1) >= 0.6.4
Provides:       crate(%{pkgname}/serde1)

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Random number generators and other randomness functionality - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/getrandom)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(rand-chacha-0.3/std) >= 0.3.1
Requires:       crate(rand-core-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
