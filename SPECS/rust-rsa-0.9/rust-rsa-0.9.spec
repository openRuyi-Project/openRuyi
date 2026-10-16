# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rsa
%global full_version 0.9.10
%global pkgname rsa-0.9

Name:           rust-rsa-0.9
Version:        0.9.10
Release:        %autorelease
Summary:        Rust crate "rsa"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/RSA
#!RemoteAsset:  sha256:b8573f03f5883dcaebdfcf4725caa1ecb9c15b2ef50c43a07b816e06799bb12d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-oid-0.9) >= 0.9.0
Requires:       crate(digest-0.10/alloc) >= 0.10.5
Requires:       crate(digest-0.10/oid) >= 0.10.5
Requires:       crate(num-bigint-dig-0.8/i128) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/prime) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/zeroize) >= 0.8.6
Requires:       crate(num-integer-0.1) >= 0.1.39
Requires:       crate(num-traits-0.2/libm) >= 0.2.9
Requires:       crate(pkcs1-0.7/alloc) >= 0.7.5
Requires:       crate(pkcs1-0.7/pkcs8) >= 0.7.5
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.2
Requires:       crate(rand-core-0.6) >= 0.6.4
Requires:       crate(signature-2/alloc) >= 2.1.0
Requires:       crate(signature-2/digest) >= 2.1.0
Requires:       crate(signature-2/rand-core) >= 2.1.0
Requires:       crate(spki-0.7/alloc) >= 0.7.3
Requires:       crate(subtle-2) >= 2.1.1
Requires:       crate(zeroize-1/alloc) >= 1.5.0
Requires:       crate(zeroize-1/default) >= 1.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Source code for takopackized Rust crate "rsa"

%package     -n %{name}+default
Summary:        Pure Rust RSA implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pem) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/u64-digit) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust RSA implementation - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6/getrandom) >= 0.6.4
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        Pure Rust RSA implementation - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-dig-0.8/i128) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/nightly) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/prime) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/zeroize) >= 0.8.6
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust RSA implementation - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs1-0.7/alloc) >= 0.7.5
Requires:       crate(pkcs1-0.7/pem) >= 0.7.5
Requires:       crate(pkcs1-0.7/pkcs8) >= 0.7.5
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.2
Requires:       crate(pkcs8-0.10/pem) >= 0.10.2
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs5
Summary:        Pure Rust RSA implementation - feature "pkcs5"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.2
Requires:       crate(pkcs8-0.10/encryption) >= 0.10.2
Provides:       crate(%{pkgname}/pkcs5) = %{version}

%description -n %{name}+pkcs5
This metapackage enables feature "pkcs5" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust RSA implementation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-dig-0.8/i128) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/prime) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/serde) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/zeroize) >= 0.8.6
Requires:       crate(serde-1/derive) >= 1.0.184
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1
Summary:        Pure Rust RSA implementation - feature "sha1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-0.10/oid) >= 0.10.5
Provides:       crate(%{pkgname}/sha1) = %{version}

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust RSA implementation - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10/oid) >= 0.10.6
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust RSA implementation - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/alloc) >= 0.10.5
Requires:       crate(digest-0.10/oid) >= 0.10.5
Requires:       crate(digest-0.10/std) >= 0.10.5
Requires:       crate(pkcs1-0.7/alloc) >= 0.7.5
Requires:       crate(pkcs1-0.7/pkcs8) >= 0.7.5
Requires:       crate(pkcs1-0.7/std) >= 0.7.5
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.2
Requires:       crate(pkcs8-0.10/std) >= 0.10.2
Requires:       crate(rand-core-0.6/std) >= 0.6.4
Requires:       crate(signature-2/alloc) >= 2.1.0
Requires:       crate(signature-2/digest) >= 2.1.0
Requires:       crate(signature-2/rand-core) >= 2.1.0
Requires:       crate(signature-2/std) >= 2.1.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+u64-digit
Summary:        Pure Rust RSA implementation - feature "u64_digit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-dig-0.8/i128) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/prime) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/u64-digit) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/zeroize) >= 0.8.6
Provides:       crate(%{pkgname}/u64-digit) = %{version}

%description -n %{name}+u64-digit
This metapackage enables feature "u64_digit" for the Rust rsa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
