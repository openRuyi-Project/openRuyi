# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name primefield
%global full_version 0.14.0-rc.11
%global pkgname primefield-0.14.0-rc.11

Name:           rust-primefield-0.14.0-rc.11
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "primefield"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/primefield
#!RemoteAsset:  sha256:b1d7e42f46a29abc16fb621a3466ee453358ebaae48a9e515f287e0af052ed8f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-bigint-0.7/hybrid-array) >= 0.7.1
Requires:       crate(crypto-bigint-0.7/rand-core) >= 0.7.1
Requires:       crate(crypto-bigint-0.7/subtle) >= 0.7.1
Requires:       crate(crypto-common-0.2/default) >= 0.2.0
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.0
Requires:       crate(ff-0.14) >= 0.14.0
Requires:       crate(rand-core-0.10) >= 0.10.0
Requires:       crate(subtle-2/const-generics) >= 2.6.0
Requires:       crate(zeroize-1) >= 1.7.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "primefield"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
