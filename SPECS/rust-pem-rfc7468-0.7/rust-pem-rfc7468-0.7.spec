# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pem-rfc7468
%global full_version 0.7.0
%global pkgname pem-rfc7468-0.7

Name:           rust-pem-rfc7468-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "pem-rfc7468"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/pem-rfc7468
#!RemoteAsset:  sha256:88b39c9bfcfc231068454382784bb460aae594343fb030d46e9f50a645418412
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64ct-1/default) >= 1.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Provides a no_std-friendly, constant-time implementation suitable for use with cryptographic private keys.
Source code for takopackized Rust crate "pem-rfc7468"

%package     -n %{name}+alloc
Summary:        PEM Encoding (RFC 7468) for PKIX, PKCS, and CMS Structures, implementing a strict subset of the original Privacy-Enhanced Mail encoding intended specifically for use with cryptographic keys, certificates, and other messages - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64ct-1/alloc) >= 1.4.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
Provides a no_std-friendly, constant-time implementation suitable for use with cryptographic private keys.
This metapackage enables feature "alloc" for the Rust pem-rfc7468 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        PEM Encoding (RFC 7468) for PKIX, PKCS, and CMS Structures, implementing a strict subset of the original Privacy-Enhanced Mail encoding intended specifically for use with cryptographic keys, certificates, and other messages - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(base64ct-1/std) >= 1.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
Provides a no_std-friendly, constant-time implementation suitable for use with cryptographic private keys.
This metapackage enables feature "std" for the Rust pem-rfc7468 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
