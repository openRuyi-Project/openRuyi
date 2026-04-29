# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name signature
%global full_version 2.2.0
%global pkgname signature-2.0

Name:           rust-signature-2.0
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "signature"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/traits/tree/master/signature
#!RemoteAsset:  sha256:77549399552de45a898a580c1b41d445bf730df867cc44e6c0233bbc4b8329de
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
ECDSA, Ed25519)
Source code for takopackized Rust crate "signature"

%package     -n %{name}+derive
Summary:        Traits for cryptographic signature algorithms (e.g - feature "derive"
Requires:       crate(%{pkgname})
Requires:       crate(signature-derive-2.0/default) >= 2.0.0
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+derive
ECDSA, Ed25519)
This metapackage enables feature "derive" for the Rust signature crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Traits for cryptographic signature algorithms (e.g - feature "digest"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10) >= 0.10.7
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
ECDSA, Ed25519)
This metapackage enables feature "digest" for the Rust signature crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for cryptographic signature algorithms (e.g - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6) >= 0.6.4
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
ECDSA, Ed25519)
This metapackage enables feature "rand_core" for the Rust signature crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Traits for cryptographic signature algorithms (e.g - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(rand-core-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
ECDSA, Ed25519)
This metapackage enables feature "std" for the Rust signature crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
