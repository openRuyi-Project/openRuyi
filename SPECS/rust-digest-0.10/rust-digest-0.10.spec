# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name digest
%global full_version 0.10.7
%global pkgname digest-0.10

Name:           rust-digest-0.10
Version:        0.10.7
Release:        %autorelease
Summary:        Rust crate "digest"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:9ed9a281f7bc9b7576e61468ba615a66a5c8cfdff42420a70aa82701a3b1e292
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.1/default) >= 0.1.3
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "digest"

%package     -n %{name}+blobby
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "blobby" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(blobby-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/blobby) = %{version}
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev" feature.

%package     -n %{name}+block-buffer
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "block-buffer" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block-buffer-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/block-buffer) = %{version}
Provides:       crate(%{pkgname}/core-api) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+block-buffer
This metapackage enables feature "block-buffer" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "core-api", and "default" features.

%package     -n %{name}+const-oid
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "const-oid" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-oid-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/const-oid) = %{version}
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+const-oid
This metapackage enables feature "const-oid" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "oid" feature.

%package     -n %{name}+rand-core
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crypto-common-0.1/rand-core) >= 0.1.3
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(crypto-common-0.1/std) >= 0.1.3
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "subtle" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(subtle-2) >= 2.4.0
Provides:       crate(%{pkgname}/mac) = %{version}
Provides:       crate(%{pkgname}/subtle) = %{version}

%description -n %{name}+subtle
This metapackage enables feature "subtle" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mac" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
