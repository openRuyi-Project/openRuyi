# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-webpki
%global full_version 0.103.10
%global pkgname rustls-webpki-0.103

Name:           rust-rustls-webpki-0.103
Version:        0.103.10
Release:        %autorelease
Summary:        Rust crate "rustls-webpki"
License:        ISC
URL:            https://github.com/rustls/webpki
#!RemoteAsset:  sha256:df33b2b81ac578cabaf06b89b0631153a3f416b0a886e8a7a1707fb51abbd1ef
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-pki-types-1.0) >= 1.14.0
Requires:       crate(untrusted-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "rustls-webpki"

%package     -n %{name}+alloc
Summary:        Web PKI X.509 Certificate Verification - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(ring-0.17/alloc) >= 0.17.14
Requires:       crate(rustls-pki-types-1.0/alloc) >= 1.14.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rustls-webpki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-rs
Summary:        Web PKI X.509 Certificate Verification - feature "aws-lc-rs"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-rs-1.0) >= 1.14
Requires:       crate(aws-lc-rs-1.0/aws-lc-sys) >= 1.14
Requires:       crate(aws-lc-rs-1.0/prebuilt-nasm) >= 1.14
Provides:       crate(%{pkgname}/aws-lc-rs)

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws-lc-rs" for the Rust rustls-webpki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-rs-fips
Summary:        Web PKI X.509 Certificate Verification - feature "aws-lc-rs-fips"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-rs-1.0) >= 1.14
Requires:       crate(aws-lc-rs-1.0/fips) >= 1.14
Provides:       crate(%{pkgname}/aws-lc-rs-fips)

%description -n %{name}+aws-lc-rs-fips
This metapackage enables feature "aws-lc-rs-fips" for the Rust rustls-webpki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-rs-unstable
Summary:        Web PKI X.509 Certificate Verification - feature "aws-lc-rs-unstable"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/aws-lc-rs)
Requires:       crate(aws-lc-rs-1.0/unstable) >= 1.14
Provides:       crate(%{pkgname}/aws-lc-rs-unstable)

%description -n %{name}+aws-lc-rs-unstable
This metapackage enables feature "aws-lc-rs-unstable" for the Rust rustls-webpki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Web PKI X.509 Certificate Verification - feature "ring"
Requires:       crate(%{pkgname})
Requires:       crate(ring-0.17) >= 0.17.14
Provides:       crate(%{pkgname}/ring)

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust rustls-webpki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Web PKI X.509 Certificate Verification - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(rustls-pki-types-1.0/std) >= 1.14.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rustls-webpki crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
