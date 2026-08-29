# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pbkdf2
%global full_version 0.13.0
%global pkgname pbkdf2-0.13

Name:           rust-pbkdf2-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "pbkdf2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/password-hashes/tree/master/pbkdf2
#!RemoteAsset:  sha256:112d82ceb8c5bf524d9af484d4e4970c9fd5a0cc15ba14ad93dccd28873b0629
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.11/default) >= 0.11.0
Requires:       crate(digest-0.11/mac) >= 0.11.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pbkdf2"

%package     -n %{name}+alloc
Summary:        Generic implementation of PBKDF2 - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mcf-0.6/alloc) >= 0.6.0
Requires:       crate(mcf-0.6/base64) >= 0.6.0
Requires:       crate(password-hash-0.6/alloc) >= 0.6.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Generic implementation of PBKDF2 - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6/getrandom) >= 0.6.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hmac
Summary:        Generic implementation of PBKDF2 - feature "hmac" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hmac-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hmac) = %{version}

%description -n %{name}+hmac
This metapackage enables feature "hmac" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+kdf
Summary:        Generic implementation of PBKDF2 - feature "kdf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Requires:       crate(kdf-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/kdf) = %{version}

%description -n %{name}+kdf
This metapackage enables feature "kdf" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mcf
Summary:        Generic implementation of PBKDF2 - feature "mcf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/password-hash) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Requires:       crate(mcf-0.6/base64) >= 0.6.0
Provides:       crate(%{pkgname}/mcf) = %{version}

%description -n %{name}+mcf
This metapackage enables feature "mcf" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+password-hash
Summary:        Generic implementation of PBKDF2 - feature "password-hash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/password-hash) = %{version}

%description -n %{name}+password-hash
This metapackage enables feature "password-hash" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phc
Summary:        Generic implementation of PBKDF2 - feature "phc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Requires:       crate(password-hash-0.6/phc) >= 0.6.0
Provides:       crate(%{pkgname}/phc) = %{version}

%description -n %{name}+phc
This metapackage enables feature "phc" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Generic implementation of PBKDF2 - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6/rand-core) >= 0.6.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Generic implementation of PBKDF2 - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hmac) = %{version}
Requires:       crate(sha2-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust pbkdf2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
