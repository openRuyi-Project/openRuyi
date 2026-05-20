# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-webpki
%global full_version 0.101.7
%global pkgname rustls-webpki-0.101

Name:           rust-rustls-webpki-0.101
Version:        0.101.7
Release:        %autorelease
Summary:        Rust crate "rustls-webpki"
License:        ISC
URL:            https://github.com/rustls/webpki
#!RemoteAsset:  sha256:8b6275d1ee7a1cd780b64aca7726599a1dbc893b1e64144529e55c3c2f745765
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ring-0.17) >= 0.17.0
Requires:       crate(untrusted-0.9/default) >= 0.9.0
Provides:       crate(rustls-webpki) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "rustls-webpki"

%package     -n %{name}+alloc
Summary:        Web PKI X.509 Certificate Verification - feature "alloc" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(ring-0.17/alloc) >= 0.17.0
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rustls-webpki crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "std" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
