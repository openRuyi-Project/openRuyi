# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name scrypt
%global full_version 0.11.0
%global pkgname scrypt-0.11

Name:           rust-scrypt-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "scrypt"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/password-hashes/tree/master/scrypt
#!RemoteAsset:  sha256:0516a385866c09368f0b5bcd1caff3366aace790fcd46e2bb032697bb172fd1f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pbkdf2-0.12/default) >= 0.12.0
Requires:       crate(salsa20-0.10) >= 0.10.2
Requires:       crate(sha2-0.10) >= 0.10.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "scrypt"

%package     -n %{name}+default
Summary:        Scrypt password-based key derivation function - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/simple) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+password-hash
Summary:        Scrypt password-based key derivation function - feature "password-hash" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.5/rand-core) >= 0.5.0
Provides:       crate(%{pkgname}/password-hash) = %{version}
Provides:       crate(%{pkgname}/simple) = %{version}

%description -n %{name}+password-hash
This metapackage enables feature "password-hash" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "simple" feature.

%package     -n %{name}+std
Summary:        Scrypt password-based key derivation function - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.5/rand-core) >= 0.5.0
Requires:       crate(password-hash-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
