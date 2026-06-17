# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name argon2
%global full_version 0.5.3
%global pkgname argon2-0.5

Name:           rust-argon2-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "argon2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/password-hashes/tree/master/argon2
#!RemoteAsset:  sha256:3c3610892ee6e0cbce8ae2700349fcf8f98adb0dbfbee85aec3c9179d29cc072
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64ct-1/default) >= 1.0.0
Requires:       crate(blake2-0.10) >= 0.10.6
Requires:       crate(cpufeatures-0.2/default) >= 0.2.12
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "argon2"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.5/alloc) >= 0.5.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/password-hash) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+password-hash
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "password-hash" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/password-hash) = %{version}
Provides:       crate(%{pkgname}/simple) = %{version}

%description -n %{name}+password-hash
This metapackage enables feature "password-hash" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "simple" feature.

%package     -n %{name}+rand
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.5/rand-core) >= 0.5.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(password-hash-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

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
