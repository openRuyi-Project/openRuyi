# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pkix-path
%global full_version 0.3.2
%global pkgname pkix-path-0.3

Name:           rust-pkix-path-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "pkix-path"
License:        Apache-2.0 OR MIT
URL:            https://github.com/MarkAtwood/crate-pkix
#!RemoteAsset:  sha256:325809ccf6e48c67f1e1e7a91187566372346797737ee00d1381a5881f76aecf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(der-0.7/default) >= 0.7.0
Requires:       crate(signature-2/default) >= 2.0.0
Requires:       crate(spki-0.7/default) >= 0.7.0
Requires:       crate(x509-cert-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pkix-path"

%package     -n %{name}+default
Summary:        RFC 5280 X.509 certificate path validation — pure Rust, no_std - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/p256) = %{version}
Requires:       crate(%{pkgname}/rsa) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust pkix-path crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+p256
Summary:        RFC 5280 X.509 certificate path validation — pure Rust, no_std - feature "p256"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(p256-0.13/ecdsa) >= 0.13.0
Requires:       crate(p256-0.13/pkcs8) >= 0.13.0
Provides:       crate(%{pkgname}/p256) = %{version}

%description -n %{name}+p256
This metapackage enables feature "p256" for the Rust pkix-path crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+p384
Summary:        RFC 5280 X.509 certificate path validation — pure Rust, no_std - feature "p384"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(p384-0.13/ecdsa) >= 0.13.0
Requires:       crate(p384-0.13/pkcs8) >= 0.13.0
Requires:       crate(sha2-0.10/oid) >= 0.10.0
Provides:       crate(%{pkgname}/p384) = %{version}

%description -n %{name}+p384
This metapackage enables feature "p384" for the Rust pkix-path crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rsa
Summary:        RFC 5280 X.509 certificate path validation — pure Rust, no_std - feature "rsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rsa-0.9) >= 0.9.0
Requires:       crate(sha2-0.10/oid) >= 0.10.0
Provides:       crate(%{pkgname}/rsa) = %{version}

%description -n %{name}+rsa
This metapackage enables feature "rsa" for the Rust pkix-path crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustcrypto
Summary:        RFC 5280 X.509 certificate path validation — pure Rust, no_std - feature "rustcrypto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/p256) = %{version}
Requires:       crate(%{pkgname}/p384) = %{version}
Requires:       crate(%{pkgname}/rsa) = %{version}
Provides:       crate(%{pkgname}/rustcrypto) = %{version}

%description -n %{name}+rustcrypto
This metapackage enables feature "rustcrypto" for the Rust pkix-path crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        RFC 5280 X.509 certificate path validation — pure Rust, no_std - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64ct-1/alloc) >= 1.0.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pkix-path crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        RFC 5280 X.509 certificate path validation — pure Rust, no_std - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.7/std) >= 0.7.0
Requires:       crate(signature-2/std) >= 2.0.0
Requires:       crate(spki-0.7/std) >= 0.7.0
Requires:       crate(x509-cert-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pkix-path crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
