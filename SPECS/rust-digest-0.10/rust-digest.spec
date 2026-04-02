# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)

%description
Source code for takopackized Rust crate "digest"

%package     -n %{name}+blobby
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "blobby" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(blobby-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/blobby)
Provides:       crate(%{pkgname}/dev)

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev" feature.

%package     -n %{name}+block-buffer
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "block-buffer" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(block-buffer-0.10/default) >= 0.10.4
Provides:       crate(%{pkgname}/block-buffer)
Provides:       crate(%{pkgname}/core-api)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+block-buffer
This metapackage enables feature "block-buffer" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "core-api", and "default" features.

%package     -n %{name}+const-oid
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "const-oid" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(const-oid-0.9/default) >= 0.9.6
Provides:       crate(%{pkgname}/const-oid)
Provides:       crate(%{pkgname}/oid)

%description -n %{name}+const-oid
This metapackage enables feature "const-oid" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "oid" feature.

%package     -n %{name}+rand-core
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(crypto-common-0.1/rand-core) >= 0.1.6
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(crypto-common-0.1/std) >= 0.1.6
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "subtle" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(%{pkgname}/mac)
Provides:       crate(%{pkgname}/subtle)

%description -n %{name}+subtle
This metapackage enables feature "subtle" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mac" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
