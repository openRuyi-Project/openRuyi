# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tls_codec
%global full_version 0.4.2
%global pkgname tls-codec-0.4

Name:           rust-tls-codec-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "tls_codec"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/tls_codec
#!RemoteAsset:  sha256:0de2e01245e2bb89d6f05801c564fa27624dbd7b1846859876c7dad82e90bf6b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zeroize-1/alloc) >= 1.8.0
Requires:       crate(zeroize-1/zeroize-derive) >= 1.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/mls) = %{version}

%description
Source code for takopackized Rust crate "tls_codec"

%package     -n %{name}+arbitrary
Summary:        Pure Rust implementation of the TLS (de)serialization - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.4.0
Requires:       crate(arbitrary-1/derive) >= 1.4.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust tls_codec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+conditional-deserialization
Summary:        Pure Rust implementation of the TLS (de)serialization - feature "conditional_deserialization"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(tls-codec-derive-0.4/conditional-deserialization) >= 0.4.2
Provides:       crate(%{pkgname}/conditional-deserialization) = %{version}

%description -n %{name}+conditional-deserialization
This metapackage enables feature "conditional_deserialization" for the Rust tls_codec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the TLS (de)serialization - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(serde-1/default) >= 1.0.184
Requires:       crate(serde-1/derive) >= 1.0.184
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust tls_codec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the TLS (de)serialization - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tls-codec-derive-0.4/std) >= 0.4.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust tls_codec crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tls-codec-derive
Summary:        Pure Rust implementation of the TLS (de)serialization - feature "tls_codec_derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tls-codec-derive-0.4/default) >= 0.4.2
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/tls-codec-derive) = %{version}

%description -n %{name}+tls-codec-derive
This metapackage enables feature "tls_codec_derive" for the Rust tls_codec crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
