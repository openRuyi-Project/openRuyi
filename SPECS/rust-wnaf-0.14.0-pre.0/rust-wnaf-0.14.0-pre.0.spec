# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wnaf
%global full_version 0.14.0-pre.0
%global pkgname wnaf-0.14.0-pre.0

Name:           rust-wnaf-0.14.0-pre.0
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "wnaf"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/wnaf
#!RemoteAsset:  sha256:81b8f9936fa4378fbe26130d702e51a9d723b22a073105500dfd80d9bb508199
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ff-0.14) >= 0.14.0
Requires:       crate(group-0.14) >= 0.14.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Contains an implementation adapted from the `group` crate which has been forked and enhanced but is otherwise compatible with that crate's traits, along with the `ff` crate's traits for finite field representations
Source code for takopackized Rust crate "wnaf"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
