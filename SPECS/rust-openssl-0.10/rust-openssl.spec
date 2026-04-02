# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssl
%global full_version 0.10.76
%global pkgname openssl-0.10

Name:           rust-openssl-0.10
Version:        0.10.76
Release:        %autorelease
Summary:        Rust crate "openssl"
License:        Apache-2.0
URL:            https://github.com/rust-openssl/rust-openssl
#!RemoteAsset:  sha256:951c002c75e16ea2c65b8c7e4d3d51d5530d8dfa7d060b4776828c88cfb18ecf
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(foreign-types-0.3/default) >= 0.3.2
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(openssl-macros-0.1/default) >= 0.1.1
Requires:       crate(openssl-sys-0.9/default) >= 0.9.112
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/v101)
Provides:       crate(%{pkgname}/v102)
Provides:       crate(%{pkgname}/v110)
Provides:       crate(%{pkgname}/v111)

%description
Source code for takopackized Rust crate "openssl"

%package     -n %{name}+aws-lc
Summary:        OpenSSL bindings - feature "aws-lc"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/aws-lc) >= 0.9.112
Provides:       crate(%{pkgname}/aws-lc)

%description -n %{name}+aws-lc
This metapackage enables feature "aws-lc" for the Rust openssl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-fips
Summary:        OpenSSL bindings - feature "aws-lc-fips"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/aws-lc-fips) >= 0.9.112
Provides:       crate(%{pkgname}/aws-lc-fips)

%description -n %{name}+aws-lc-fips
This metapackage enables feature "aws-lc-fips" for the Rust openssl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bindgen
Summary:        OpenSSL bindings - feature "bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/bindgen) >= 0.9.112
Provides:       crate(%{pkgname}/bindgen)

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust openssl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-boringssl
Summary:        OpenSSL bindings - feature "unstable_boringssl"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/unstable-boringssl) >= 0.9.112
Provides:       crate(%{pkgname}/unstable-boringssl)

%description -n %{name}+unstable-boringssl
This metapackage enables feature "unstable_boringssl" for the Rust openssl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored
Summary:        OpenSSL bindings - feature "vendored"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.112
Provides:       crate(%{pkgname}/vendored)

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust openssl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
