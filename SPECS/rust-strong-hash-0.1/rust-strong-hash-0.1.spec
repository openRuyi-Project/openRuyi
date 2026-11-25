# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strong_hash
%global full_version 0.1.0
%global pkgname strong-hash-0.1

Name:           rust-strong-hash-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "strong_hash"
License:        MIT OR Apache-2.0
URL:            https://github.com/facebook/buck2
#!RemoteAsset:  sha256:0831334aea34390b6b6ec7af0a27f9ee6324ad3a69463e6b240d83d6b7bce9c9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ref-cast-1/default) >= 1.0.18
Requires:       crate(strong-hash-derive-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "strong_hash"

%package     -n %{name}+num-bigint
Summary:        Hash trait similar to std::hash::Hash but for strong/cryptographic hashes - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust strong_hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+triomphe
Summary:        Hash trait similar to std::hash::Hash but for strong/cryptographic hashes - feature "triomphe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(triomphe-0.1/default) >= 0.1.8
Provides:       crate(%{pkgname}/triomphe) = %{version}

%description -n %{name}+triomphe
This metapackage enables feature "triomphe" for the Rust strong_hash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
