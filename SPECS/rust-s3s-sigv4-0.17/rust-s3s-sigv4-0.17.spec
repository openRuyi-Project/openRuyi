# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name s3s-sigv4
%global full_version 0.17.0
%global pkgname s3s-sigv4-0.17

Name:           rust-s3s-sigv4-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "s3s-sigv4"
License:        Apache-2.0
URL:            https://github.com/Nugine/s3s
#!RemoteAsset:  sha256:330996b9a24804b3df4ad37e62e7817968857d99cf6029c21512b6b64b97f645
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7/default) >= 0.7.8
Requires:       crate(base64-simd-0.8/default) >= 0.8.0
Requires:       crate(hex-simd-0.8/default) >= 0.8.0
Requires:       crate(hmac-0.13/default) >= 0.13.0
Requires:       crate(jiff-0.2/default) >= 0.2.35
Requires:       crate(nom-8/default) >= 8.0.0
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(sha2-0.11/default) >= 0.11.0
Requires:       crate(smallvec-1/default) >= 1.15.2
Requires:       crate(std-next-0.1/default) >= 0.1.9
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(zeroize-1/default) >= 1.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "s3s-sigv4"

%package     -n %{name}+openssl
Summary:        AWS Signature Version 4: parsing, canonicalization, and signing - feature "openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-0.10/default) >= 0.10.81
Provides:       crate(%{pkgname}/openssl) = %{version}

%description -n %{name}+openssl
This metapackage enables feature "openssl" for the Rust s3s-sigv4 crate, by
pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
