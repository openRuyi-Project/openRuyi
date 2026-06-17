# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name digest
%global full_version 0.11.3
%global pkgname digest-0.11

Name:           rust-digest-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "digest"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:f1dd6dbb5841937940781866fa1281a1ff7bd3bf827091440879f9994983d5c2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "digest"

%package     -n %{name}+blobby
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "blobby" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(blobby-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/blobby) = %{version}
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev" feature.

%package     -n %{name}+block-api
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "block-api" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block-buffer-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/block-api) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+block-api
This metapackage enables feature "block-api" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+getrandom
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(crypto-common-0.2/getrandom) >= 0.2.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mac
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "mac"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ctutils-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/mac) = %{version}

%description -n %{name}+mac
This metapackage enables feature "mac" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "oid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-oid-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block-buffer-0.12/zeroize) >= 0.12.0
Requires:       crate(zeroize-1) >= 1.7.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
