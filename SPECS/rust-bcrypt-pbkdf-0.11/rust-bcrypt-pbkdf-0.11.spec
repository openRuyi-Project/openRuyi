# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bcrypt-pbkdf
%global full_version 0.11.0
%global pkgname bcrypt-pbkdf-0.11

Name:           rust-bcrypt-pbkdf-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "bcrypt-pbkdf"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/password-hashes/tree/master/bcrypt-pbkdf
#!RemoteAsset:  sha256:144e573728da132683b9488acd528274c790e07fc06ff81ee29f9d8f8b1041e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(blowfish-0.10/bcrypt) >= 0.10.0
Requires:       crate(blowfish-0.10/default) >= 0.10.0
Requires:       crate(pbkdf2-0.13) >= 0.13.0
Requires:       crate(sha2-0.11) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bcrypt-pbkdf"

%package     -n %{name}+zeroize
Summary:        Bcrypt-pbkdf password-based key derivation function - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust bcrypt-pbkdf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
