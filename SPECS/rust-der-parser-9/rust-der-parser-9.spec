# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name der-parser
%global full_version 9.0.0
%global pkgname der-parser-9

Name:           rust-der-parser-9
Version:        9.0.0
Release:        %autorelease
Summary:        Rust crate "der-parser"
License:        MIT OR Apache-2.0
URL:            https://github.com/rusticata/der-parser
#!RemoteAsset:  sha256:5cd0a5c643689626bec213c4d8bd4d96acc8ffdb4ad4bb6bc16abf27d5f4b553
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(asn1-rs-0.6/default) >= 0.6.0
Requires:       crate(displaydoc-0.2) >= 0.2.0
Requires:       crate(nom-7/default) >= 7.0.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Requires:       crate(rusticata-macros-4/default) >= 4.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "der-parser"

%package     -n %{name}+cookie-factory
Summary:        Parser/encoder for ASN.1 BER/DER data - feature "cookie-factory"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cookie-factory-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/cookie-factory) = %{version}

%description -n %{name}+cookie-factory
This metapackage enables feature "cookie-factory" for the Rust der-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Parser/encoder for ASN.1 BER/DER data - feature "num-bigint" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/bigint) = %{version}
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust der-parser crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bigint" feature.

%package     -n %{name}+serialize
Summary:        Parser/encoder for ASN.1 BER/DER data - feature "serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cookie-factory) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serialize
This metapackage enables feature "serialize" for the Rust der-parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
