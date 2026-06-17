# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crypto-bigint
%global full_version 0.7.3
%global pkgname crypto-bigint-0.7

Name:           rust-crypto-bigint-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "crypto-bigint"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/crypto-bigint
#!RemoteAsset:  sha256:42a0d26b245348befa0c121944541476763dcc46ede886c88f9d12e1697d27c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cpubits-0.1/default) >= 0.1.0
Requires:       crate(ctutils-0.4/default) >= 0.4.0
Requires:       crate(num-traits-0.2) >= 0.2.19
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/extra-sizes) = %{version}

%description
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
Source code for takopackized Rust crate "crypto-bigint"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "alloc" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+der
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "der"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/der) = %{version}

%description -n %{name}+der
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "der" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(getrandom-0.4/sys-rng) >= 0.4.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "getrandom" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hybrid-array
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "hybrid-array"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hybrid-array-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}/hybrid-array) = %{version}

%description -n %{name}+hybrid-array
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "hybrid-array" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "rand_core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "rand_core" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+rlp
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "rlp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rlp-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/rlp) = %{version}

%description -n %{name}+rlp
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "rlp" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "serde" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "subtle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ctutils-0.4/subtle) >= 0.4.0
Requires:       crate(hybrid-array-0.4/subtle) >= 0.4.8
Requires:       crate(subtle-2) >= 2.6.0
Provides:       crate(%{pkgname}/subtle) = %{version}

%description -n %{name}+subtle
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "subtle" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "zeroize" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
