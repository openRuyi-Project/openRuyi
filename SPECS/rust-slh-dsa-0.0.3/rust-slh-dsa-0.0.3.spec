# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name slh-dsa
%global full_version 0.0.3
%global pkgname slh-dsa-0.0.3

Name:           rust-slh-dsa-0.0.3
Version:        0.0.3
Release:        %autorelease
Summary:        Rust crate "slh-dsa"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/slh-dsa
#!RemoteAsset:  sha256:bd2f20f4049197e03db1104a6452f4d9e96665d79f880198dce4a7026ba5f267
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-oid-0.9/db) >= 0.9.0
Requires:       crate(const-oid-0.9/default) >= 0.9.0
Requires:       crate(digest-0.10/default) >= 0.10.0
Requires:       crate(hmac-0.12/default) >= 0.12.0
Requires:       crate(hybrid-array-0.3/default) >= 0.3.0
Requires:       crate(hybrid-array-0.3/extra-sizes) >= 0.3.0
Requires:       crate(pkcs8-0.10) >= 0.10.0
Requires:       crate(rand-core-0.6/default) >= 0.6.0
Requires:       crate(sha2-0.10) >= 0.10.0
Requires:       crate(sha3-0.10) >= 0.10.0
Requires:       crate(signature-2/default) >= 2.2.0
Requires:       crate(signature-2/rand-core) >= 2.2.0
Requires:       crate(typenum-1/const-generics) >= 1.17.0
Requires:       crate(typenum-1/default) >= 1.17.0
Requires:       crate(zerocopy-0.7/default) >= 0.7.34
Requires:       crate(zerocopy-0.7/derive) >= 0.7.34

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "slh-dsa"

%package     -n %{name}+default
Summary:        Pure Rust implementation of SLH-DSA (aka SPHINCS+) as described in the FIPS-205 standard - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.0
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust slh-dsa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
