# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name const-oid
%global full_version 0.9.6
%global pkgname const-oid-0.9

Name:           rust-const-oid-0.9
Version:        0.9.6
Release:        %autorelease
Summary:        Rust crate "const-oid"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/const-oid
#!RemoteAsset:  sha256:c2459377285ad874054d797f3ccebf984978aa39129f6eafde5cdc8315b612f8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/db)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
embedded) support
Source code for takopackized Rust crate "const-oid"

%package     -n %{name}+arbitrary
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard as defined in ITU X.660, with support for BER/DER encoding/decoding as well as heapless no_std (i.e - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.2
Requires:       crate(arbitrary-1.0/derive) >= 1.2
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
embedded) support
This metapackage enables feature "arbitrary" for the Rust const-oid crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
