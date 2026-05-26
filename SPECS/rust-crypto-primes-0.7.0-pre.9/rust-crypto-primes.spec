# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crypto-primes
%global full_version 0.7.0-pre.9
%global pkgname crypto-primes-0.7.0-pre.9

Name:           rust-crypto-primes-0.7.0-pre.9
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "crypto-primes"
License:        Apache-2.0 OR MIT
URL:            https://github.com/entropyxyz/crypto-primes
#!RemoteAsset:  sha256:6081ce8b60c0e533e2bba42771b94eb6149052115f4179744d5779883dc98583
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-bigint-0.7.0-rc.28/rand-core) >= 0.7.0-rc.28
Requires:       crate(libm-0.2/arch) >= 0.2.16
Requires:       crate(rand-core-0.10) >= 0.10.1
Provides:       crate(crypto-primes) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/tests-exhaustive)

%description
Source code for takopackized Rust crate "crypto-primes"

%package     -n %{name}+glass-pumpkin
Summary:        Random prime number generation and primality checking library - feature "glass_pumpkin" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glass-pumpkin-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/glass-pumpkin)
Provides:       crate(%{pkgname}/tests-glass-pumpkin)

%description -n %{name}+glass-pumpkin
This metapackage enables feature "glass_pumpkin" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tests-glass-pumpkin" feature.

%package     -n %{name}+openssl
Summary:        Random prime number generation and primality checking library - feature "openssl" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(openssl-0.10/default) >= 0.10.39
Requires:       crate(openssl-0.10/vendored) >= 0.10.39
Provides:       crate(%{pkgname}/openssl)
Provides:       crate(%{pkgname}/tests-openssl)

%description -n %{name}+openssl
This metapackage enables feature "openssl" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tests-openssl" feature.

%package     -n %{name}+rayon
Summary:        Random prime number generation and primality checking library - feature "rayon" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/multicore)
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "multicore" feature.

%package     -n %{name}+rug
Summary:        Random prime number generation and primality checking library - feature "rug"
Requires:       crate(%{pkgname})
Requires:       crate(rug-1.0/integer) >= 1.26
Provides:       crate(%{pkgname}/rug)

%description -n %{name}+rug
This metapackage enables feature "rug" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tests-all
Summary:        Random prime number generation and primality checking library - feature "tests-all"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/tests-exhaustive)
Requires:       crate(%{pkgname}/tests-glass-pumpkin)
Requires:       crate(%{pkgname}/tests-gmp)
Requires:       crate(%{pkgname}/tests-openssl)
Provides:       crate(%{pkgname}/tests-all)

%description -n %{name}+tests-all
This metapackage enables feature "tests-all" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tests-gmp
Summary:        Random prime number generation and primality checking library - feature "tests-gmp"
Requires:       crate(%{pkgname})
Requires:       crate(rug-1.0/integer) >= 1.26
Requires:       crate(rug-1.0/std) >= 1.26
Provides:       crate(%{pkgname}/tests-gmp)

%description -n %{name}+tests-gmp
This metapackage enables feature "tests-gmp" for the Rust crypto-primes crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
