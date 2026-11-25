# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name oid-registry
%global full_version 0.8.1
%global pkgname oid-registry-0.8

Name:           rust-oid-registry-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "oid-registry"
License:        MIT OR Apache-2.0
URL:            https://github.com/rusticata/oid-registry
#!RemoteAsset:  sha256:12f40cff3dde1b6087cc5d5f5d4d65712f34016a03ed60e9c08dcc392736b5b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(asn1-rs-0.7/default) >= 0.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/kdf) = %{version}
Provides:       crate(%{pkgname}/ms-spc) = %{version}
Provides:       crate(%{pkgname}/nist-algs) = %{version}
Provides:       crate(%{pkgname}/pkcs1) = %{version}
Provides:       crate(%{pkgname}/pkcs12) = %{version}
Provides:       crate(%{pkgname}/pkcs7) = %{version}
Provides:       crate(%{pkgname}/pkcs9) = %{version}
Provides:       crate(%{pkgname}/registry) = %{version}
Provides:       crate(%{pkgname}/x500) = %{version}
Provides:       crate(%{pkgname}/x509) = %{version}
Provides:       crate(%{pkgname}/x962) = %{version}

%description
Source code for takopackized Rust crate "oid-registry"

%package     -n %{name}+crypto
Summary:        Object Identifier (OID) database - feature "crypto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kdf) = %{version}
Requires:       crate(%{pkgname}/nist-algs) = %{version}
Requires:       crate(%{pkgname}/pkcs1) = %{version}
Requires:       crate(%{pkgname}/pkcs12) = %{version}
Requires:       crate(%{pkgname}/pkcs7) = %{version}
Requires:       crate(%{pkgname}/pkcs9) = %{version}
Requires:       crate(%{pkgname}/x962) = %{version}
Provides:       crate(%{pkgname}/crypto) = %{version}

%description -n %{name}+crypto
This metapackage enables feature "crypto" for the Rust oid-registry crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
