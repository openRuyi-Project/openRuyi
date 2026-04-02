# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hkdf
%global full_version 0.12.4
%global pkgname hkdf-0.12

Name:           rust-hkdf-0.12
Version:        0.12.4
Release:        %autorelease
Summary:        Rust crate "hkdf"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/KDFs/
#!RemoteAsset:  sha256:7b5f8eb2ad728638ea2c7d47a21db23b7b58a72ed6a38256b8a1849f15fbbdf7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hmac-0.12/default) >= 0.12.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "hkdf"

%package     -n %{name}+std
Summary:        HMAC-based Extract-and-Expand Key Derivation Function (HKDF) - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(hmac-0.12/std) >= 0.12.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust hkdf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
