# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asn1-rs
%global full_version 0.6.2
%global pkgname asn1-rs-0.6

Name:           rust-asn1-rs-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "asn1-rs"
License:        MIT OR Apache-2.0
URL:            https://github.com/rusticata/asn1-rs
#!RemoteAsset:  sha256:5493c3bedbacf7fd7382c6346bbd66687d12bbaad3a89a2d2c303ee6cf20b048
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(asn1-rs-derive-0.5/default) >= 0.5.0
Requires:       crate(asn1-rs-impl-0.2/default) >= 0.2.0
Requires:       crate(displaydoc-0.2/default) >= 0.2.2
Requires:       crate(nom-7/std) >= 7.0.0
Requires:       crate(num-traits-0.2/default) >= 0.2.14
Requires:       crate(rusticata-macros-4/default) >= 4.0.0
Requires:       crate(thiserror-1/default) >= 1.0.25
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "asn1-rs"

%package     -n %{name}+bitvec
Summary:        Parser/encoder for ASN.1 BER/DER data - feature "bitvec" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitvec-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bits) = %{version}
Provides:       crate(%{pkgname}/bitvec) = %{version}

%description -n %{name}+bitvec
This metapackage enables feature "bitvec" for the Rust asn1-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bits" feature.

%package     -n %{name}+colored
Summary:        Parser/encoder for ASN.1 BER/DER data - feature "colored" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(colored-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/colored) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/trace) = %{version}

%description -n %{name}+colored
This metapackage enables feature "colored" for the Rust asn1-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "debug", and "trace" features.

%package     -n %{name}+cookie-factory
Summary:        Parser/encoder for ASN.1 BER/DER data - feature "cookie-factory" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cookie-factory-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/cookie-factory) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+cookie-factory
This metapackage enables feature "cookie-factory" for the Rust asn1-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serialize" feature.

%package     -n %{name}+num-bigint
Summary:        Parser/encoder for ASN.1 BER/DER data - feature "num-bigint" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/bigint) = %{version}
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust asn1-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bigint" feature.

%package     -n %{name}+time
Summary:        Parser/encoder for ASN.1 BER/DER data - feature "time" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.0
Requires:       crate(time-0.3/formatting) >= 0.3.0
Requires:       crate(time-0.3/macros) >= 0.3.0
Requires:       crate(time-0.3/parsing) >= 0.3.0
Provides:       crate(%{pkgname}/datetime) = %{version}
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust asn1-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "datetime" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
