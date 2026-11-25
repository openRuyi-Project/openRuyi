# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pkix-revocation
%global full_version 0.3.3
%global pkgname pkix-revocation-0.3

Name:           rust-pkix-revocation-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "pkix-revocation"
License:        Apache-2.0 OR MIT
URL:            https://github.com/MarkAtwood/crate-pkix
#!RemoteAsset:  sha256:da3b442616fbb7b036180da1830f4877bfa09e7cbe38d06aa78c64d4dadbeafc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(der-0.7/default) >= 0.7.0
Requires:       crate(pkix-path-0.3/default) >= 0.3.2
Requires:       crate(spki-0.7/default) >= 0.7.0
Requires:       crate(x509-cert-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pkix-revocation"

%package     -n %{name}+ocsp
Summary:        Certificate revocation checking (CRL, OCSP) for pkix-path - feature "ocsp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(sha1-0.10/oid) >= 0.10.0
Requires:       crate(sha2-0.10/oid) >= 0.10.0
Requires:       crate(x509-ocsp-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/ocsp) = %{version}

%description -n %{name}+ocsp
This metapackage enables feature "ocsp" for the Rust pkix-revocation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Certificate revocation checking (CRL, OCSP) for pkix-path - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkix-path-0.3/serde) >= 0.3.2
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pkix-revocation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Certificate revocation checking (CRL, OCSP) for pkix-path - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.7/std) >= 0.7.0
Requires:       crate(pkix-path-0.3/std) >= 0.3.2
Provides:       crate(%{pkgname}/crl) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pkix-revocation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "crl" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
