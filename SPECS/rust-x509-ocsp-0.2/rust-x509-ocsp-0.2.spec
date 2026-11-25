# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name x509-ocsp
%global full_version 0.2.1
%global pkgname x509-ocsp-0.2

Name:           rust-x509-ocsp-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "x509-ocsp"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/x509-ocsp
#!RemoteAsset:  sha256:5e54e695a31f0fecb826cf59ae2093c941d7ef932a1f8508185dd23b29ce2e2e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-oid-0.9/db) >= 0.9.5
Requires:       crate(der-0.7/alloc) >= 0.7.8
Requires:       crate(der-0.7/default) >= 0.7.8
Requires:       crate(der-0.7/derive) >= 0.7.8
Requires:       crate(der-0.7/oid) >= 0.7.8
Requires:       crate(spki-0.7/alloc) >= 0.7.2
Requires:       crate(spki-0.7/default) >= 0.7.2
Requires:       crate(x509-cert-0.2) >= 0.2.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "x509-ocsp"

%package     -n %{name}+builder
Summary:        Pure Rust implementation of the X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP formats as described in RFC 6960 - feature "builder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/signature) = %{version}
Provides:       crate(%{pkgname}/builder) = %{version}

%description -n %{name}+builder
This metapackage enables feature "builder" for the Rust x509-ocsp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP formats as described in RFC 6960 - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/oid) >= 0.10.7
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust x509-ocsp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of the X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP formats as described in RFC 6960 - feature "rand_core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6) >= 0.6.4
Provides:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust x509-ocsp crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rand" feature.

%package     -n %{name}+signature
Summary:        Pure Rust implementation of the X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP formats as described in RFC 6960 - feature "signature"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-2/digest) >= 2.1.0
Requires:       crate(signature-2/rand-core) >= 2.1.0
Provides:       crate(%{pkgname}/signature) = %{version}

%description -n %{name}+signature
This metapackage enables feature "signature" for the Rust x509-ocsp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP formats as described in RFC 6960 - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.7/alloc) >= 0.7.8
Requires:       crate(der-0.7/derive) >= 0.7.8
Requires:       crate(der-0.7/oid) >= 0.7.8
Requires:       crate(der-0.7/std) >= 0.7.8
Requires:       crate(x509-cert-0.2/std) >= 0.2.4
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust x509-ocsp crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
