# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wnaf
%global full_version 0.14.1
%global pkgname wnaf-0.14

Name:           rust-wnaf-0.14
Version:        0.14.1
Release:        %autorelease
Summary:        Rust crate "wnaf"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/wnaf
#!RemoteAsset:  sha256:795ca18b3fdb5e62bf982199278341ddcf7ebf7d32e25e212ad05d496e95f6fa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ff-0.14) >= 0.14.0
Requires:       crate(group-0.14) >= 0.14.0
Requires:       crate(hybrid-array-0.4/default) >= 0.4.13
Requires:       crate(primefield-0.14) >= 0.14.0

Provides:       crate(%{pkgname}) = %{version}

%description
Contains an implementation adapted from the `group` crate which has been forked and enhanced but is otherwise compatible with that crate's traits, along with the `ff` crate's traits for finite field representations
Source code for takopackized Rust crate "wnaf"

%package     -n %{name}+alloc
Summary:        WNAF (w-ary non-adjacent form) variable-time scalar multiplication implemented generically over elliptic curve groups with full `no_alloc` support, including multiscalar multiplication using Straus's interleaved window method - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ff-0.14/alloc) >= 0.14.0
Requires:       crate(group-0.14/alloc) >= 0.14.0
Requires:       crate(hybrid-array-0.4/alloc) >= 0.4.13
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+alloc
Contains an implementation adapted from the `group` crate which has been forked and enhanced but is otherwise compatible with that crate's traits, along with the `ff` crate's traits for finite field representations
This metapackage enables feature "alloc" for the Rust wnaf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
