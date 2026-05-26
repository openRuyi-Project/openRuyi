# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cbc
%global full_version 0.2.0
%global pkgname cbc-0.2

Name:           rust-cbc-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "cbc"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-modes
#!RemoteAsset:  sha256:98db6aeaef0eeef2c1e3ce9a27b739218825dae116076352ac3777076aa22225
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.5/default) >= 0.5.1
Provides:       crate(cbc) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "cbc"

%package     -n %{name}+alloc
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(cipher-0.5/alloc) >= 0.5.1
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust cbc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block-padding
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation - feature "block-padding" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(cipher-0.5/block-padding) >= 0.5.1
Provides:       crate(%{pkgname}/block-padding)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+block-padding
This metapackage enables feature "block-padding" for the Rust cbc crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+zeroize
Summary:        Cipher Block Chaining (CBC) block cipher mode of operation - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(cipher-0.5/zeroize) >= 0.5.1
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust cbc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
