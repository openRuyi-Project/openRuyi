# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name x509-parser
%global full_version 0.16.0
%global pkgname x509-parser-0.16

Name:           rust-x509-parser-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "x509-parser"
License:        MIT OR Apache-2.0
URL:            https://github.com/rusticata/x509-parser
#!RemoteAsset:  sha256:fcbc162f30700d6f3f82a24bf7cc62ffe7caea42c0b2cba8bf7f3ae50cf51f69
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(asn1-rs-0.6/datetime) >= 0.6.1
Requires:       crate(asn1-rs-0.6/default) >= 0.6.1
Requires:       crate(data-encoding-2/default) >= 2.2.1
Requires:       crate(der-parser-9/bigint) >= 9.0.0
Requires:       crate(der-parser-9/default) >= 9.0.0
Requires:       crate(lazy-static-1/default) >= 1.4.0
Requires:       crate(nom-7/default) >= 7.0.0
Requires:       crate(oid-registry-0.7/crypto) >= 0.7.0
Requires:       crate(oid-registry-0.7/default) >= 0.7.0
Requires:       crate(oid-registry-0.7/x509) >= 0.7.0
Requires:       crate(oid-registry-0.7/x962) >= 0.7.0
Requires:       crate(rusticata-macros-4/default) >= 4.0.0
Requires:       crate(thiserror-1/default) >= 1.0.2
Requires:       crate(time-0.3/default) >= 0.3.20
Requires:       crate(time-0.3/formatting) >= 0.3.20
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/validate) = %{version}

%description
Source code for takopackized Rust crate "x509-parser"

%package     -n %{name}+ring
Summary:        Parser for the X.509 v3 format (RFC 5280 certificates) - feature "ring" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.17/default) >= 0.17.7
Provides:       crate(%{pkgname}/ring) = %{version}
Provides:       crate(%{pkgname}/verify) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust x509-parser crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "verify" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
