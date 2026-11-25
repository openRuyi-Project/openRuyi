# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ssh-encoding
%global full_version 0.3.0
%global pkgname ssh-encoding-0.3

Name:           rust-ssh-encoding-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "ssh-encoding"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/SSH/tree/master/ssh-encoding
#!RemoteAsset:  sha256:7b54d0ed0498daf3f78d82e00e28c8eec9d75a067c4cfbcc7a0f7d0f4077749e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ssh-encoding"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64ct-1/alloc) >= 1.8.0
Requires:       crate(pem-rfc7468-1/alloc) >= 1.0.0
Requires:       crate(zeroize-1/alloc) >= 1.8.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64ct-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigint
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Requires:       crate(crypto-bigint-0.7/alloc) >= 0.7.0
Provides:       crate(%{pkgname}/bigint) = %{version}

%description -n %{name}+bigint
This metapackage enables feature "bigint" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bytes-1) >= 1.11.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctutils
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "ctutils"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ctutils-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/ctutils) = %{version}

%description -n %{name}+ctutils
This metapackage enables feature "ctutils" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(pem-rfc7468-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ssh-derive
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "ssh-derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ssh-derive-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/ssh-derive) = %{version}

%description -n %{name}+ssh-derive
This metapackage enables feature "ssh-derive" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.8.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
