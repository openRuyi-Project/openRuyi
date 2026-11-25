# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name argon2
%global full_version 0.6.0
%global pkgname argon2-0.6

Name:           rust-argon2-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "argon2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/password-hashes/tree/master/argon2
#!RemoteAsset:  sha256:134c52ddac6d63c576bef8168db10c83c49c26444ecbc68060fef078925a901c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64ct-1/default) >= 1.7.0
Requires:       crate(blake2-0.11) >= 0.11.0
Requires:       crate(cpufeatures-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "argon2"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6/alloc) >= 0.6.0
Requires:       crate(password-hash-0.6/phc) >= 0.6.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(%{pkgname}/password-hash) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6/getrandom) >= 0.6.0
Requires:       crate(password-hash-0.6/phc) >= 0.6.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kdf
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "kdf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(kdf-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/kdf) = %{version}

%description -n %{name}+kdf
This metapackage enables feature "kdf" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.7.0
Provides:       crate(%{pkgname}/parallel) = %{version}

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+password-hash
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "password-hash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6/default) >= 0.6.0
Requires:       crate(password-hash-0.6/phc) >= 0.6.0
Provides:       crate(%{pkgname}/password-hash) = %{version}

%description -n %{name}+password-hash
This metapackage enables feature "password-hash" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6/phc) >= 0.6.0
Requires:       crate(password-hash-0.6/rand-core) >= 0.6.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
