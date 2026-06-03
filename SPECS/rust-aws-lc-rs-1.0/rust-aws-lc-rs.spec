# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aws-lc-rs
%global full_version 1.15.2
%global pkgname aws-lc-rs-1.0

Name:           rust-aws-lc-rs-1.0
Version:        1.15.2
Release:        %autorelease
Summary:        Rust crate "aws-lc-rs"
License:        ISC AND (Apache-2.0 OR ISC)
URL:            https://github.com/aws/aws-lc-rs
#!RemoteAsset:  sha256:6a88aab2464f1f25453baa7a07c84c5b7684e274054ba06817f382357f77a288
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zeroize-1.0/default) >= 1.8.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/test-logging)
Provides:       crate(%{pkgname}/unstable)

%description
This library strives to be API-compatible with the popular Rust library named ring.
Source code for takopackized Rust crate "aws-lc-rs"

%package     -n %{name}+aws-lc-sys
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "aws-lc-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-sys-0.35) >= 0.35.0
Provides:       crate(%{pkgname}/aws-lc-sys)
Provides:       crate(%{pkgname}/non-fips)

%description -n %{name}+aws-lc-sys
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "aws-lc-sys" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "non-fips" feature.

%package     -n %{name}+prebuilt-nasm
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "prebuilt-nasm"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-sys-0.35/prebuilt-nasm) >= 0.35.0
Provides:       crate(%{pkgname}/prebuilt-nasm)

%description -n %{name}+prebuilt-nasm
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "prebuilt-nasm" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
