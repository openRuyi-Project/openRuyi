# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dsa
%global full_version 0.6.3
%global pkgname dsa-0.6

Name:           rust-dsa-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "dsa"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/dsa
#!RemoteAsset:  sha256:48bc224a9084ad760195584ce5abb3c2c34a225fa312a128ad245a6b412b7689
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.10/default) >= 0.10.0
Requires:       crate(num-bigint-dig-0.8/prime) >= 0.8.0
Requires:       crate(num-bigint-dig-0.8/rand) >= 0.8.0
Requires:       crate(num-bigint-dig-0.8/zeroize) >= 0.8.0
Requires:       crate(num-traits-0.2) >= 0.2.0
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.0
Requires:       crate(rfc6979-0.4/default) >= 0.4.0
Requires:       crate(sha2-0.10) >= 0.10.0
Requires:       crate(signature-2/alloc) >= 2.0.0
Requires:       crate(signature-2/digest) >= 2.0.0
Requires:       crate(signature-2/rand-core) >= 2.0.0
Requires:       crate(zeroize-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "dsa"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
