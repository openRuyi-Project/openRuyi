# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name spki
%global full_version 0.8.0
%global pkgname spki-0.8

Name:           rust-spki-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "spki"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/spki
#!RemoteAsset:  sha256:1d9efca8738c78ee9484207732f728b1ef517bbb1833d6fc0879ca898a522f6f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(der-0.8/default) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
OIDs)
Source code for takopackized Rust crate "spki"

%package     -n %{name}+alloc
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64ct-1/alloc) >= 1.0.0
Requires:       crate(der-0.8/alloc) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
OIDs)
This metapackage enables feature "alloc" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arbitrary
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.4.0
Requires:       crate(arbitrary-1/derive) >= 1.4.0
Requires:       crate(der-0.8/arbitrary) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
OIDs)
This metapackage enables feature "arbitrary" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64ct-1) >= 1.0.0
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
OIDs)
This metapackage enables feature "base64" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
OIDs)
This metapackage enables feature "digest" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fingerprint
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "fingerprint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/fingerprint) = %{version}

%description -n %{name}+fingerprint
OIDs)
This metapackage enables feature "fingerprint" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(der-0.8/pem) >= 0.8.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
OIDs)
This metapackage enables feature "pem" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
OIDs)
This metapackage enables feature "sha2" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(der-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
OIDs)
This metapackage enables feature "std" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
