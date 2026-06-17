# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name der
%global full_version 0.7.10
%global pkgname der-0.7

Name:           rust-der-0.7
Version:        0.7.10
Release:        %autorelease
Summary:        Rust crate "der"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/der
#!RemoteAsset:  sha256:e7c1832837b905bbfb5101e07cc24c8deddf52f93225eee6ead5f4d63d53ddcb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/real) = %{version}

%description
Source code for takopackized Rust crate "der"

%package     -n %{name}+alloc
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/alloc) >= 1.5.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+arbitrary
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.3.0
Requires:       crate(arbitrary-1/derive) >= 1.3.0
Requires:       crate(const-oid-0.9/arbitrary) >= 0.9.2
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bytes-1) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-derive-0.7/default) >= 0.7.2
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flagset
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets - feature "flagset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flagset-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/flagset) = %{version}

%description -n %{name}+flagset
This metapackage enables feature "flagset" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets - feature "oid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-oid-0.9/default) >= 0.9.2
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Requires:       crate(pem-rfc7468-0.7/alloc) >= 0.7.0
Requires:       crate(pem-rfc7468-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3) >= 0.3.4
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.5.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
