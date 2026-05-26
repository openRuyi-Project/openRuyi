# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aes
%global full_version 0.8.4
%global pkgname aes-0.8

Name:           rust-aes-0.8
Version:        0.8.4
Release:        %autorelease
Summary:        Rust crate "aes"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-ciphers
#!RemoteAsset:  sha256:b169f7a6d4742236a0a00c541b845991d0ac43e546831af1249753ab4c3aa3a0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(cipher-0.4/default) >= 0.4.4
Requires:       crate(cpufeatures-0.2/default) >= 0.2.17
Provides:       crate(aes) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/hazmat)

%description
Rijndael)
Source code for takopackized Rust crate "aes"

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the Advanced Encryption Standard (a.k.a - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.6.0
Requires:       crate(zeroize-1.0/aarch64) >= 1.5.6
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
Rijndael)
This metapackage enables feature "zeroize" for the Rust aes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
