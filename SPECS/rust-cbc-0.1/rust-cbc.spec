# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cbc
%global full_version 0.1.2
%global pkgname cbc-0.1

Name:           rust-cbc-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "cbc"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-modes
#!RemoteAsset:  sha256:26b52a9543ae338f279b96b0b9fed9c8093744685043739079ce85cd58f289a6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.4/default) >= 0.4.4
Provides:       crate(cbc) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "cbc"

%package     -n %{name}+alloc
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(cipher-0.4/alloc) >= 0.4.4
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust cbc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block-padding
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation - feature "block-padding" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(cipher-0.4/block-padding) >= 0.4.4
Provides:       crate(%{pkgname}/block-padding)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+block-padding
This metapackage enables feature "block-padding" for the Rust cbc crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+std
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(cipher-0.4/std) >= 0.4.4
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust cbc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(cipher-0.4/zeroize) >= 0.4.4
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust cbc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
