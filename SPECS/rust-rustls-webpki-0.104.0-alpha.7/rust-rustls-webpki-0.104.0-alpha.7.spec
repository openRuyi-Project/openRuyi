# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-webpki
%global full_version 0.104.0-alpha.7
%global pkgname rustls-webpki-0.104.0-alpha.7

Name:           rust-rustls-webpki-0.104.0-alpha.7
Version:        0.104.0
Release:        %autorelease
Summary:        Rust crate "rustls-webpki"
License:        ISC
URL:            https://github.com/rustls/webpki
#!RemoteAsset:  sha256:bea702cca24d344fc70973022bf7eb920c224e318466eb49784272337dd24b1a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-pki-types-1) >= 1.13.0
Requires:       crate(untrusted-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rustls-webpki"

%package     -n %{name}+alloc
Summary:        Web PKI X.509 Certificate Verification - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pki-types-1/alloc) >= 1.13.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rustls-webpki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Web PKI X.509 Certificate Verification - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(rustls-pki-types-1/std) >= 1.13.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rustls-webpki crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
