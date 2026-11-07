# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand
%global full_version 0.7.3
%global pkgname rand-0.7

Name:           rust-rand-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "rand"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand
#!RemoteAsset:  sha256:6a6b1679d49b24bbfe0c803429aa1874472f50d9b363131f0e89fc356b544d03
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-chacha-0.2) >= 0.2.1
Requires:       crate(rand-core-0.5/default) >= 0.5.1
Requires:       crate(rand-hc-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/serde1) = %{version}

%description
Source code for takopackized Rust crate "rand"

%package     -n %{name}+alloc
Summary:        Random number generators and other randomness functionality - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.5/alloc) >= 0.5.1
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Random number generators and other randomness functionality - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/getrandom-package) = %{version}
Requires:       crate(rand-core-0.5/getrandom) >= 0.5.1
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom-package
Summary:        Random number generators and other randomness functionality - feature "getrandom_package"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}/getrandom-package) = %{version}

%description -n %{name}+getrandom-package
This metapackage enables feature "getrandom_package" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Random number generators and other randomness functionality - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.22
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Random number generators and other randomness functionality - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+packed-simd
Summary:        Random number generators and other randomness functionality - feature "packed_simd" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(packed-simd-0.3/default) >= 0.3.0
Requires:       crate(packed-simd-0.3/into-bits) >= 0.3.0
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/packed-simd) = %{version}
Provides:       crate(%{pkgname}/simd-support) = %{version}

%description -n %{name}+packed-simd
This metapackage enables feature "packed_simd" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nightly", and "simd_support" features.

%package     -n %{name}+rand-pcg
Summary:        Random number generators and other randomness functionality - feature "rand_pcg" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-pcg-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/rand-pcg) = %{version}
Provides:       crate(%{pkgname}/small-rng) = %{version}

%description -n %{name}+rand-pcg
This metapackage enables feature "rand_pcg" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "small_rng" feature.

%package     -n %{name}+std
Summary:        Random number generators and other randomness functionality - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(rand-chacha-0.2/std) >= 0.2.1
Requires:       crate(rand-core-0.5/std) >= 0.5.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+stdweb
Summary:        Random number generators and other randomness functionality - feature "stdweb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.1/stdweb) >= 0.1.1
Provides:       crate(%{pkgname}/stdweb) = %{version}

%description -n %{name}+stdweb
This metapackage enables feature "stdweb" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Random number generators and other randomness functionality - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.1/wasm-bindgen) >= 0.1.1
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
