# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name webpki
%global full_version 0.22.4
%global pkgname webpki-0.22

Name:           rust-webpki-0.22
Version:        0.22.4
Release:        %autorelease
Summary:        Rust crate "webpki"
License:        FIXME
URL:            https://github.com/briansmith/webpki
#!RemoteAsset:  sha256:ed63aea5ce73d0ff405984102c42de94fc55a6b75765d621c65262469b3c9b53
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ring-0.17) >= 0.17.2
Requires:       crate(untrusted-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "webpki"

%package     -n %{name}+alloc
Summary:        Web PKI X.509 Certificate Verification - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.17/alloc) >= 0.17.2
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust webpki crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
