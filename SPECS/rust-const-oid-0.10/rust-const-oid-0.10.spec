# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name const-oid
%global full_version 0.10.2
%global pkgname const-oid-0.10

Name:           rust-const-oid-0.10
Version:        0.10.2
Release:        %autorelease
Summary:        Rust crate "const-oid"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/const-oid
#!RemoteAsset:  sha256:a6ef517f0926dd24a1582492c791b6a4818a4d94e789a334894aa15b0d12f55c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/db) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
embedded) support
Source code for takopackized Rust crate "const-oid"

%package     -n %{name}+arbitrary
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard as defined in ITU X.660, with support for BER/DER encoding/decoding as well as heapless no_std (i.e - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.4.0
Requires:       crate(arbitrary-1/derive) >= 1.4.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
embedded) support
This metapackage enables feature "arbitrary" for the Rust const-oid crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
