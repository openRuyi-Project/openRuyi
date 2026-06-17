# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ssh-encoding
%global full_version 0.2.0
%global pkgname ssh-encoding-0.2

Name:           rust-ssh-encoding-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "ssh-encoding"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/SSH/tree/master/ssh-encoding
#!RemoteAsset:  sha256:eb9242b9ef4108a78e8cd1a2c98e193ef372437f8c22be363075233321dd4a15
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
Requires:       crate(base64ct-1/alloc) >= 1.4.0
Requires:       crate(pem-rfc7468-0.7/alloc) >= 0.7.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64ct-1/default) >= 1.4.0
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bytes-1) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(pem-rfc7468-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of SSH data type decoders/encoders as described in RFC4251 - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(base64ct-1/std) >= 1.4.0
Requires:       crate(pem-rfc7468-0.7/std) >= 0.7.0
Requires:       crate(sha2-0.10/std) >= 0.10.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ssh-encoding crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
