# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aws-lc-fips-sys
%global full_version 0.14.2
%global pkgname aws-lc-fips-sys-0.14

Name:           rust-aws-lc-fips-sys-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "aws-lc-fips-sys"
License:        ISC AND (Apache-2.0 OR ISC) AND OpenSSL
URL:            https://github.com/aws/aws-lc-rs
#!RemoteAsset:  sha256:03367707e92796b190a4207d4d39b0a4271d574503d2969c2b0cfbf5c87658ee
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bindgen-0.72/default) >= 0.72.0
Requires:       crate(cc-1) >= 1.2.26
Requires:       crate(cmake-0.1) >= 0.1.54
Requires:       crate(dunce-1) >= 1.0.5
Requires:       crate(fs-extra-1) >= 1.3.0
Requires:       crate(pkg-config-0.3) >= 0.3.31
Requires:       crate(regex-1/default) >= 1.11.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/asan) = %{version}
Provides:       crate(%{pkgname}/bindgen) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fips) = %{version}
Provides:       crate(%{pkgname}/ssl) = %{version}

%description
This is the FIPS validated version of AWS-LC.
Source code for takopackized Rust crate "aws-lc-fips-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
