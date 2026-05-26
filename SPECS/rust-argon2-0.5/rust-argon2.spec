# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64ct-1.0/default) >= 1.8.3
Requires:       crate(blake2-0.10) >= 0.10.6
Requires:       crate(cpufeatures-0.2/default) >= 0.2.17
Provides:       crate(argon2) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "argon2"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(password-hash-0.5/alloc) >= 0.5.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/password-hash)
Requires:       crate(%{pkgname}/rand)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+password-hash
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "password-hash" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(password-hash-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/password-hash)
Provides:       crate(%{pkgname}/simple)

%description -n %{name}+password-hash
This metapackage enables feature "password-hash" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "simple" feature.

%package     -n %{name}+rand
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(password-hash-0.5/rand-core) >= 0.5.0
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(password-hash-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the Argon2 password hashing function with support for the Argon2d, Argon2i, and Argon2id algorithmic variants - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust argon2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
