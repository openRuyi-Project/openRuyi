# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssl-sys
%global full_version 0.9.112
%global pkgname openssl-sys-0.9

Name:           rust-openssl-sys-0.9
Version:        0.9.112
Release:        %autorelease
Summary:        Rust crate "openssl-sys"
License:        MIT
URL:            https://github.com/rust-openssl/rust-openssl
#!RemoteAsset:  sha256:57d55af3b3e226502be1526dfdba67ab0e9c96fc293004e79576b2b9edb0dbdb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.58
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Requires:       crate(vcpkg-0.2/default) >= 0.2.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "openssl-sys"

%package     -n %{name}+aws-lc
Summary:        FFI bindings to OpenSSL - feature "aws-lc"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-sys-0.38/default) >= 0.38.0
Requires:       crate(aws-lc-sys-0.38/ssl) >= 0.38.0
Provides:       crate(%{pkgname}/aws-lc)

%description -n %{name}+aws-lc
This metapackage enables feature "aws-lc" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-fips
Summary:        FFI bindings to OpenSSL - feature "aws-lc-fips"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-fips-sys-0.13/bindgen) >= 0.13.0
Requires:       crate(aws-lc-fips-sys-0.13/default) >= 0.13.0
Requires:       crate(aws-lc-fips-sys-0.13/ssl) >= 0.13.0
Provides:       crate(%{pkgname}/aws-lc-fips)

%description -n %{name}+aws-lc-fips
This metapackage enables feature "aws-lc-fips" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bindgen
Summary:        FFI bindings to OpenSSL - feature "bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(bindgen-0.72/default) >= 0.72.0
Requires:       crate(bindgen-0.72/experimental) >= 0.72.0
Provides:       crate(%{pkgname}/bindgen)

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bssl-sys
Summary:        FFI bindings to OpenSSL - feature "bssl-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bssl-sys-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/bssl-sys)
Provides:       crate(%{pkgname}/unstable-boringssl)

%description -n %{name}+bssl-sys
This metapackage enables feature "bssl-sys" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable_boringssl" feature.

%package     -n %{name}+openssl-src
Summary:        FFI bindings to OpenSSL - feature "openssl-src" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(openssl-src-300.0/default) >= 300.5.5
Requires:       crate(openssl-src-300.0/legacy) >= 300.5.5
Provides:       crate(%{pkgname}/openssl-src)
Provides:       crate(%{pkgname}/vendored)

%description -n %{name}+openssl-src
This metapackage enables feature "openssl-src" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "vendored" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
