# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name x509-cert
%global full_version 0.2.5
%global pkgname x509-cert-0.2

Name:           rust-x509-cert-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "x509-cert"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/x509-cert
#!RemoteAsset:  sha256:1301e935010a701ae5f8655edc0ad17c44bad3ac5ce8c39185f75453b720ae94
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-oid-0.9/db) >= 0.9.3
Requires:       crate(const-oid-0.9/default) >= 0.9.3
Requires:       crate(der-0.7/alloc) >= 0.7.6
Requires:       crate(der-0.7/default) >= 0.7.6
Requires:       crate(der-0.7/derive) >= 0.7.6
Requires:       crate(der-0.7/flagset) >= 0.7.6
Requires:       crate(der-0.7/oid) >= 0.7.6
Requires:       crate(spki-0.7/alloc) >= 0.7.3
Requires:       crate(spki-0.7/default) >= 0.7.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Source code for takopackized Rust crate "x509-cert"

%package     -n %{name}+arbitrary
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.3.0
Requires:       crate(arbitrary-1/derive) >= 1.3.0
Requires:       crate(der-0.7/alloc) >= 0.7.6
Requires:       crate(der-0.7/arbitrary) >= 0.7.6
Requires:       crate(der-0.7/derive) >= 0.7.6
Requires:       crate(der-0.7/flagset) >= 0.7.6
Requires:       crate(der-0.7/oid) >= 0.7.6
Requires:       crate(spki-0.7/alloc) >= 0.7.3
Requires:       crate(spki-0.7/arbitrary) >= 0.7.3
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+builder
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "builder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/signature) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(sha1-0.10/default) >= 0.10.6
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

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.7/alloc) >= 0.7.6
Requires:       crate(der-0.7/derive) >= 0.7.6
Requires:       crate(der-0.7/flagset) >= 0.7.6
Requires:       crate(der-0.7/oid) >= 0.7.6
Requires:       crate(der-0.7/pem) >= 0.7.6
Requires:       crate(spki-0.7/alloc) >= 0.7.3
Requires:       crate(spki-0.7/pem) >= 0.7.3
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

%package     -n %{name}+sha1
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "sha1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-0.10/default) >= 0.10.6
Provides:       crate(%{pkgname}/sha1) = %{version}

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signature
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "signature"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-2/default) >= 2.1.0
Requires:       crate(signature-2/rand-core) >= 2.1.0
Provides:       crate(%{pkgname}/signature) = %{version}

%description -n %{name}+signature
This metapackage enables feature "signature" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certificate format as described in RFC 5280 - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-oid-0.9/db) >= 0.9.3
Requires:       crate(const-oid-0.9/std) >= 0.9.3
Requires:       crate(der-0.7/alloc) >= 0.7.6
Requires:       crate(der-0.7/derive) >= 0.7.6
Requires:       crate(der-0.7/flagset) >= 0.7.6
Requires:       crate(der-0.7/oid) >= 0.7.6
Requires:       crate(der-0.7/std) >= 0.7.6
Requires:       crate(spki-0.7/alloc) >= 0.7.3
Requires:       crate(spki-0.7/std) >= 0.7.3
Requires:       crate(tls-codec-0.4/derive) >= 0.4.0
Requires:       crate(tls-codec-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust x509-cert crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
