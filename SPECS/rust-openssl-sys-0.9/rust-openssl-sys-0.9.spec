# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssl-sys
%global full_version 0.9.117
%global pkgname openssl-sys-0.9

Name:           rust-openssl-sys-0.9
Version:        0.9.117
Release:        %autorelease
Summary:        Rust crate "openssl-sys"
License:        MIT
URL:            https://github.com/rust-openssl/rust-openssl
#!RemoteAsset:  sha256:b47e7e6bb2c38cd930d25a23b40fa52e068c10e85f3e03a7f5ba5aaca5713695
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.61
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pkg-config-0.3) >= 0.3.9
Requires:       crate(vcpkg-0.2) >= 0.2.8
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "openssl-sys"

%package     -n %{name}+aws-lc
Summary:        FFI bindings to OpenSSL - feature "aws-lc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-sys-0.41/default) >= 0.41.0
Requires:       crate(aws-lc-sys-0.41/ssl) >= 0.41.0
Provides:       crate(%{pkgname}/aws-lc) = %{version}

%description -n %{name}+aws-lc
This metapackage enables feature "aws-lc" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-fips
Summary:        FFI bindings to OpenSSL - feature "aws-lc-fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-fips-sys-0.13/bindgen) >= 0.13.0
Requires:       crate(aws-lc-fips-sys-0.13/default) >= 0.13.0
Requires:       crate(aws-lc-fips-sys-0.13/ssl) >= 0.13.0
Provides:       crate(%{pkgname}/aws-lc-fips) = %{version}

%description -n %{name}+aws-lc-fips
This metapackage enables feature "aws-lc-fips" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bindgen
Summary:        FFI bindings to OpenSSL - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.72/default) >= 0.72.0
Requires:       crate(bindgen-0.72/experimental) >= 0.72.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bssl-sys
Summary:        FFI bindings to OpenSSL - feature "bssl-sys" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bssl-sys-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/bssl-sys) = %{version}
Provides:       crate(%{pkgname}/unstable-boringssl) = %{version}

%description -n %{name}+bssl-sys
This metapackage enables feature "bssl-sys" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable_boringssl" feature.

%package     -n %{name}+openssl-src
Summary:        FFI bindings to OpenSSL - feature "openssl-src" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-src-300/default) >= 300.2.0
Requires:       crate(openssl-src-300/legacy) >= 300.2.0
Provides:       crate(%{pkgname}/openssl-src) = %{version}
Provides:       crate(%{pkgname}/vendored) = %{version}

%description -n %{name}+openssl-src
This metapackage enables feature "openssl-src" for the Rust openssl-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "vendored" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
