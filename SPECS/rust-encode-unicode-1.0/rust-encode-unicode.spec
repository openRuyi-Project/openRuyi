# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encode_unicode
%global full_version 1.0.0
%global pkgname encode-unicode-1.0

Name:           rust-encode-unicode-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "encode_unicode"
License:        Apache-2.0 OR MIT
URL:            https://github.com/tormol/encode_unicode
#!RemoteAsset:  sha256:34aa73646ffb006b8f5147f3dc182bd4bcb190227ce861fc4a4844bf8e3cb2c0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(encode-unicode) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "encode_unicode"

%package     -n %{name}+ascii
Summary:        UTF-8 and UTF-16 character types, iterators and related methods for char, u8 and u16 - feature "ascii"
Requires:       crate(%{pkgname})
Requires:       crate(ascii-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/ascii)

%description -n %{name}+ascii
This metapackage enables feature "ascii" for the Rust encode_unicode crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
