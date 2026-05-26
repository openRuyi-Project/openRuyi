# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bcrypt-pbkdf
%global full_version 0.10.0
%global pkgname bcrypt-pbkdf-0.10

Name:           rust-bcrypt-pbkdf-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "bcrypt-pbkdf"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/password-hashes/tree/master/bcrypt-pbkdf
#!RemoteAsset:  sha256:6aeac2e1fe888769f34f05ac343bbef98b14d1ffb292ab69d4608b3abc86f2a2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(blowfish-0.9/bcrypt) >= 0.9.1
Requires:       crate(blowfish-0.9/default) >= 0.9.1
Requires:       crate(pbkdf2-0.12) >= 0.12.2
Requires:       crate(sha2-0.10) >= 0.10.9
Provides:       crate(bcrypt-pbkdf) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "bcrypt-pbkdf"

%package     -n %{name}+default
Summary:        Bcrypt-pbkdf password-based key derivation function - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bcrypt-pbkdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Bcrypt-pbkdf password-based key derivation function - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust bcrypt-pbkdf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
