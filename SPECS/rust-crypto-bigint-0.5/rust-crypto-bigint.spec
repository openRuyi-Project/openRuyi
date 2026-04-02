# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crypto-bigint
%global full_version 0.5.5
%global pkgname crypto-bigint-0.5

Name:           rust-crypto-bigint-0.5
Version:        0.5.5
Release:        %autorelease
Summary:        Rust crate "crypto-bigint"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/crypto-bigint
#!RemoteAsset:  sha256:0dc92fb57ca44df6db8059111ab3af99a63d5d0f8375d9972e319a379c6bab76
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/extra-sizes)

%description
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
Source code for takopackized Rust crate "crypto-bigint"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(serdect-0.2/alloc) >= 0.2.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "alloc" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+der
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "der"
Requires:       crate(%{pkgname})
Requires:       crate(der-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/der)

%description -n %{name}+der
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "der" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generic-array
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "generic-array"
Requires:       crate(%{pkgname})
Requires:       crate(generic-array-0.14/default) >= 0.14.9
Provides:       crate(%{pkgname}/generic-array)

%description -n %{name}+generic-array
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "generic-array" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "rand" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "rand" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6/default) >= 0.6.4
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "rand_core" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rlp
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "rlp"
Requires:       crate(%{pkgname})
Requires:       crate(rlp-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/rlp)

%description -n %{name}+rlp
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "rlp" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serdect-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "serde" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
This metapackage enables feature "zeroize" for the Rust crypto-bigint crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
