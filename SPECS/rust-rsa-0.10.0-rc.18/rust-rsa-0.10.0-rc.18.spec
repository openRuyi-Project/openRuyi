# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rsa
%global full_version 0.10.0-rc.18
%global pkgname rsa-0.10.0-rc.18

Name:           rust-rsa-0.10.0-rc.18
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "rsa"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/RSA
#!RemoteAsset:  sha256:30b2aa4ba0d89f73d1e332df05be0eeab8840351c36ca5654341dfdb57bb3caf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-oid-0.10) >= 0.10.0
Requires:       crate(crypto-bigint-0.7/alloc) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/zeroize) >= 0.7.0
Requires:       crate(crypto-primes-0.7) >= 0.7.0
Requires:       crate(digest-0.11/alloc) >= 0.11.0
Requires:       crate(digest-0.11/oid) >= 0.11.0
Requires:       crate(rand-core-0.10) >= 0.10.0
Requires:       crate(signature-3.0.0-rc.10/alloc) >= 3.0.0-rc.10
Requires:       crate(signature-3.0.0-rc.10/digest) >= 3.0.0-rc.10
Requires:       crate(signature-3.0.0-rc.10/rand-core) >= 3.0.0-rc.10
Requires:       crate(zeroize-1/alloc) >= 1.8.0
Requires:       crate(zeroize-1/default) >= 1.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Source code for takopackized Rust crate "rsa"

%package     -n %{name}+crypto-common
Summary:        Pure Rust RSA implementation - feature "crypto-common"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crypto-common-0.2/default) >= 0.2.0
Requires:       crate(crypto-common-0.2/getrandom) >= 0.2.0
Provides:       crate(%{pkgname}/crypto-common) = %{version}

%description -n %{name}+crypto-common
This metapackage enables feature "crypto-common" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust RSA implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/encoding) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encoding
Summary:        Pure Rust RSA implementation - feature "encoding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs1-0.8.0-rc.4/alloc) >= 0.8.0-rc.4
Requires:       crate(pkcs1-0.8.0-rc.4/pem) >= 0.8.0-rc.4
Requires:       crate(pkcs8-0.11/alloc) >= 0.11.0
Requires:       crate(pkcs8-0.11/pem) >= 0.11.0
Requires:       crate(spki-0.8/alloc) >= 0.8.0
Provides:       crate(%{pkgname}/encoding) = %{version}

%description -n %{name}+encoding
This metapackage enables feature "encoding" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust RSA implementation - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/crypto-common) = %{version}
Requires:       crate(crypto-bigint-0.7/alloc) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/getrandom) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/zeroize) >= 0.7.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs5
Summary:        Pure Rust RSA implementation - feature "pkcs5"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs8-0.11/alloc) >= 0.11.0
Requires:       crate(pkcs8-0.11/encryption) >= 0.11.0
Requires:       crate(pkcs8-0.11/pem) >= 0.11.0
Provides:       crate(%{pkgname}/pkcs5) = %{version}

%description -n %{name}+pkcs5
This metapackage enables feature "pkcs5" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust RSA implementation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/encoding) = %{version}
Requires:       crate(crypto-bigint-0.7/alloc) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/serde) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/zeroize) >= 0.7.0
Requires:       crate(serde-1/derive) >= 1.0.184
Requires:       crate(serdect-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1
Summary:        Pure Rust RSA implementation - feature "sha1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-0.11/oid) >= 0.11.0
Provides:       crate(%{pkgname}/sha1) = %{version}

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust RSA implementation - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.11/oid) >= 0.11.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust RSA implementation - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs1-0.8.0-rc.4/alloc) >= 0.8.0-rc.4
Requires:       crate(pkcs1-0.8.0-rc.4/pem) >= 0.8.0-rc.4
Requires:       crate(pkcs1-0.8.0-rc.4/std) >= 0.8.0-rc.4
Requires:       crate(pkcs8-0.11/alloc) >= 0.11.0
Requires:       crate(pkcs8-0.11/pem) >= 0.11.0
Requires:       crate(pkcs8-0.11/std) >= 0.11.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
