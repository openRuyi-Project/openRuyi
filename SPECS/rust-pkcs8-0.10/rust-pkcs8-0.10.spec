# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pkcs8
%global full_version 0.10.2
%global pkgname pkcs8-0.10

Name:           rust-pkcs8-0.10
Version:        0.10.2
Release:        %autorelease
Summary:        Rust crate "pkcs8"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/pkcs8
#!RemoteAsset:  sha256:f950b2377845cebe5cf8b5165cb3cc1a5e0fa5cfa3e1f7f55707d8fd82e0a7b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(der-0.7/default) >= 0.7.0
Requires:       crate(der-0.7/oid) >= 0.7.0
Requires:       crate(spki-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pkcs8"

%package     -n %{name}+3des
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "3des"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/encryption) = %{version}
Requires:       crate(pkcs5-0.7/3des) >= 0.7.0
Provides:       crate(%{pkgname}/3des) = %{version}

%description -n %{name}+3des
This metapackage enables feature "3des" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.7/alloc) >= 0.7.0
Requires:       crate(der-0.7/oid) >= 0.7.0
Requires:       crate(der-0.7/zeroize) >= 0.7.0
Requires:       crate(spki-0.7/alloc) >= 0.7.1
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+des-insecure
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "des-insecure"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/encryption) = %{version}
Requires:       crate(pkcs5-0.7/des-insecure) >= 0.7.0
Provides:       crate(%{pkgname}/des-insecure) = %{version}

%description -n %{name}+des-insecure
This metapackage enables feature "des-insecure" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encryption
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "encryption"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(pkcs5-0.7/alloc) >= 0.7.0
Requires:       crate(pkcs5-0.7/pbes2) >= 0.7.0
Provides:       crate(%{pkgname}/encryption) = %{version}

%description -n %{name}+encryption
This metapackage enables feature "encryption" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6/getrandom) >= 0.6.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(der-0.7/oid) >= 0.7.0
Requires:       crate(der-0.7/pem) >= 0.7.0
Requires:       crate(spki-0.7/pem) >= 0.7.1
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs5
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "pkcs5"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs5-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/pkcs5) = %{version}

%description -n %{name}+pkcs5
This metapackage enables feature "pkcs5" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1-insecure
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "sha1-insecure"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/encryption) = %{version}
Requires:       crate(pkcs5-0.7/sha1-insecure) >= 0.7.0
Provides:       crate(%{pkgname}/sha1-insecure) = %{version}

%description -n %{name}+sha1-insecure
This metapackage enables feature "sha1-insecure" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(der-0.7/oid) >= 0.7.0
Requires:       crate(der-0.7/std) >= 0.7.0
Requires:       crate(spki-0.7/std) >= 0.7.1
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8: Private-Key Information Syntax Specification (RFC 5208), with additional support for PKCS#8v2 asymmetric key packages (RFC 5958) - feature "subtle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(subtle-2) >= 2.0.0
Provides:       crate(%{pkgname}/subtle) = %{version}

%description -n %{name}+subtle
This metapackage enables feature "subtle" for the Rust pkcs8 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
