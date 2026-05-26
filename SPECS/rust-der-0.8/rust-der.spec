# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name der
%global full_version 0.8.0
%global pkgname der-0.8

Name:           rust-der-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "der"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/der
#!RemoteAsset:  sha256:71fd89660b2dc699704064e59e9dba0147b903e85319429e131620d022be411b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(der) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/ber)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/real)

%description
Source code for takopackized Rust crate "der"

%package     -n %{name}+alloc
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "alloc" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0/alloc) >= 1.8.2
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+arbitrary
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(arbitrary-1.0/default) >= 1.4
Requires:       crate(arbitrary-1.0/derive) >= 1.4
Requires:       crate(const-oid-0.10/arbitrary) >= 0.10.2
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "bytes"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(bytes-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bytes)

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "derive"
Requires:       crate(%{pkgname})
Requires:       crate(der-derive-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flagset
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "flagset"
Requires:       crate(%{pkgname})
Requires:       crate(flagset-0.4/default) >= 0.4.7
Provides:       crate(%{pkgname}/flagset)

%description -n %{name}+flagset
This metapackage enables feature "flagset" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heapless
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "heapless"
Requires:       crate(%{pkgname})
Requires:       crate(heapless-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/heapless)

%description -n %{name}+heapless
This metapackage enables feature "heapless" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "oid"
Requires:       crate(%{pkgname})
Requires:       crate(const-oid-0.10/default) >= 0.10.2
Provides:       crate(%{pkgname}/oid)

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/zeroize)
Requires:       crate(pem-rfc7468-1.0/alloc) >= 1.0.0
Requires:       crate(pem-rfc7468-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "time"
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3) >= 0.3.4
Provides:       crate(%{pkgname}/time)

%description -n %{name}+time
This metapackage enables feature "time" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless `no_std`/`no_alloc` targets - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust der crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
