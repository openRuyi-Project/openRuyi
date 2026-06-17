# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-bigint-dig
%global full_version 0.8.6
%global pkgname num-bigint-dig-0.8

Name:           rust-num-bigint-dig-0.8
Version:        0.8.6
Release:        %autorelease
Summary:        Rust crate "num-bigint-dig"
License:        MIT OR Apache-2.0
URL:            https://github.com/dignifiedquire/num-bigint
#!RemoteAsset:  sha256:e661dda6640fad38e827a6d4a310ff4763082116fe217f279885c97f511bb0b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/spin-no-std) >= 1.2.0
Requires:       crate(libm-0.2/default) >= 0.2.1
Requires:       crate(num-integer-0.1/i128) >= 0.1.39
Requires:       crate(num-iter-0.1) >= 0.1.37
Requires:       crate(num-traits-0.2/i128) >= 0.2.4
Requires:       crate(smallvec-1) >= 1.10.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/i128) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/u64-digit) = %{version}

%description
Source code for takopackized Rust crate "num-bigint-dig"

%package     -n %{name}+arbitrary
Summary:        Big integer implementation for Rust - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Big integer implementation for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/u64-digit) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fuzz
Summary:        Big integer implementation for Rust - feature "fuzz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arbitrary) = %{version}
Requires:       crate(smallvec-1/arbitrary) >= 1.10.0
Provides:       crate(%{pkgname}/fuzz) = %{version}

%description -n %{name}+fuzz
This metapackage enables feature "fuzz" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prime
Summary:        Big integer implementation for Rust - feature "prime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8/std-rng) >= 0.8.3
Provides:       crate(%{pkgname}/prime) = %{version}

%description -n %{name}+prime
This metapackage enables feature "prime" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Big integer implementation for Rust - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8) >= 0.8.3
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Big integer implementation for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Big integer implementation for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-integer-0.1/i128) >= 0.1.39
Requires:       crate(num-integer-0.1/std) >= 0.1.39
Requires:       crate(num-traits-0.2/i128) >= 0.2.4
Requires:       crate(num-traits-0.2/std) >= 0.2.4
Requires:       crate(rand-0.8/std) >= 0.8.3
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Requires:       crate(smallvec-1/write) >= 1.10.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Big integer implementation for Rust - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.5.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust num-bigint-dig crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
