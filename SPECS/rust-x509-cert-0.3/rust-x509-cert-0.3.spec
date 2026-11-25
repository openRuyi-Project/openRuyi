# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name x509-cert
%global full_version 0.3.0
%global pkgname x509-cert-0.3

Name:           rust-x509-cert-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "x509-cert"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/x509-cert
#!RemoteAsset:  sha256:105ef4642d9cb137ef83d623d0e4bf08b8adf69e9918ca904a174adb6d3d038b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-oid-0.10/db) >= 0.10.0
Requires:       crate(const-oid-0.10/default) >= 0.10.0
Requires:       crate(der-0.8/alloc) >= 0.8.0
Requires:       crate(der-0.8/default) >= 0.8.0
Requires:       crate(der-0.8/derive) >= 0.8.0
Requires:       crate(der-0.8/flagset) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(spki-0.8/alloc) >= 0.8.0
Requires:       crate(spki-0.8/default) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Source code for takopackized Rust crate "x509-cert"

%package     -n %{name}+arbitrary
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.4.0
Requires:       crate(arbitrary-1/derive) >= 1.4.0
Requires:       crate(der-0.8/alloc) >= 0.8.0
Requires:       crate(der-0.8/arbitrary) >= 0.8.0
Requires:       crate(der-0.8/derive) >= 0.8.0
Requires:       crate(der-0.8/flagset) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(spki-0.8/alloc) >= 0.8.0
Requires:       crate(spki-0.8/arbitrary) >= 0.8.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spki-0.8/alloc) >= 0.8.0
Requires:       crate(spki-0.8/base64) >= 0.8.0
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+builder
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "builder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/signature) = %{version}
Requires:       crate(sha1-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/builder) = %{version}

%description -n %{name}+builder
This metapackage enables feature "builder" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pem) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11) >= 0.11.0
Requires:       crate(spki-0.8/alloc) >= 0.8.0
Requires:       crate(spki-0.8/digest) >= 0.8.0
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fingerprint
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "fingerprint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spki-0.8/alloc) >= 0.8.0
Requires:       crate(spki-0.8/fingerprint) >= 0.8.0
Provides:       crate(%{pkgname}/fingerprint) = %{version}

%description -n %{name}+fingerprint
This metapackage enables feature "fingerprint" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.8/alloc) >= 0.8.0
Requires:       crate(der-0.8/derive) >= 0.8.0
Requires:       crate(der-0.8/flagset) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(der-0.8/pem) >= 0.8.0
Requires:       crate(spki-0.8/alloc) >= 0.8.0
Requires:       crate(spki-0.8/pem) >= 0.8.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sct
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "sct"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tls-codec-0.4/derive) >= 0.4.0
Provides:       crate(%{pkgname}/sct) = %{version}

%description -n %{name}+sct
This metapackage enables feature "sct" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signature
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "signature"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-3/default) >= 3.0.0
Requires:       crate(signature-3/rand-core) >= 3.0.0
Provides:       crate(%{pkgname}/signature) = %{version}

%description -n %{name}+signature
This metapackage enables feature "signature" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.8/alloc) >= 0.8.0
Requires:       crate(der-0.8/derive) >= 0.8.0
Requires:       crate(der-0.8/flagset) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(der-0.8/std) >= 0.8.0
Requires:       crate(spki-0.8/alloc) >= 0.8.0
Requires:       crate(spki-0.8/std) >= 0.8.0
Requires:       crate(tls-codec-0.4/derive) >= 0.4.0
Requires:       crate(tls-codec-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
