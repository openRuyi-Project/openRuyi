# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crypto-primes
%global full_version 0.7.2
%global pkgname crypto-primes-0.7

Name:           rust-crypto-primes-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "crypto-primes"
License:        Apache-2.0 OR MIT
URL:            https://github.com/entropyxyz/crypto-primes
#!RemoteAsset:  sha256:3633a51a39c69ebbaa4feaa694bd83d241e4093901c84a0963b19d9bb3f0cf8f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-bigint-0.7/rand-core) >= 0.7.0
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/tests-exhaustive) = %{version}

%description
Source code for takopackized Rust crate "crypto-primes"

%package     -n %{name}+glass-pumpkin
Summary:        Random prime number generation and primality checking library - feature "glass_pumpkin" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glass-pumpkin-2.0.0-rc.0/default) >= 2.0.0-rc.0
Provides:       crate(%{pkgname}/glass-pumpkin) = %{version}
Provides:       crate(%{pkgname}/tests-glass-pumpkin) = %{version}

%description -n %{name}+glass-pumpkin
This metapackage enables feature "glass_pumpkin" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tests-glass-pumpkin" feature.

%package     -n %{name}+openssl
Summary:        Random prime number generation and primality checking library - feature "openssl" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-0.10/default) >= 0.10.39
Requires:       crate(openssl-0.10/vendored) >= 0.10.39
Provides:       crate(%{pkgname}/openssl) = %{version}
Provides:       crate(%{pkgname}/tests-openssl) = %{version}

%description -n %{name}+openssl
This metapackage enables feature "openssl" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tests-openssl" feature.

%package     -n %{name}+rayon
Summary:        Random prime number generation and primality checking library - feature "rayon" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1) >= 1.0.0
Provides:       crate(%{pkgname}/multicore) = %{version}
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "multicore" feature.

%package     -n %{name}+rug
Summary:        Random prime number generation and primality checking library - feature "rug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rug-1/integer) >= 1.26.0
Provides:       crate(%{pkgname}/rug) = %{version}

%description -n %{name}+rug
This metapackage enables feature "rug" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tests-all
Summary:        Random prime number generation and primality checking library - feature "tests-all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tests-exhaustive) = %{version}
Requires:       crate(%{pkgname}/tests-glass-pumpkin) = %{version}
Requires:       crate(%{pkgname}/tests-gmp) = %{version}
Requires:       crate(%{pkgname}/tests-openssl) = %{version}
Provides:       crate(%{pkgname}/tests-all) = %{version}

%description -n %{name}+tests-all
This metapackage enables feature "tests-all" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tests-gmp
Summary:        Random prime number generation and primality checking library - feature "tests-gmp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rug-1/integer) >= 1.26.0
Requires:       crate(rug-1/std) >= 1.26.0
Provides:       crate(%{pkgname}/tests-gmp) = %{version}

%description -n %{name}+tests-gmp
This metapackage enables feature "tests-gmp" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
