# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aws-lc-rs
%global full_version 1.17.0
%global pkgname aws-lc-rs-1.0

Name:           rust-aws-lc-rs-1.0
Version:        1.17.0
Release:        %autorelease
Summary:        Rust crate "aws-lc-rs"
License:        ISC AND (Apache-2.0 OR ISC)
URL:            https://github.com/aws/aws-lc-rs
#!RemoteAsset:  sha256:5ec2f1fc3ec205783a5da9a7e6c1509cc69dedf09a1949e412c1e18469326d00
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zeroize-1.0/default) >= 1.8.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/dev-tests-only)
Provides:       crate(%{pkgname}/test-logging)
Provides:       crate(%{pkgname}/unstable)

%description
This library strives to be API-compatible with the popular Rust library named ring.
Source code for takopackized Rust crate "aws-lc-rs"

%package     -n %{name}+asan
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "asan"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-fips-sys-0.13/asan) >= 0.13.1
Requires:       crate(aws-lc-sys-0.41/asan) >= 0.41.0
Provides:       crate(%{pkgname}/asan)

%description -n %{name}+asan
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "asan" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-sys
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "aws-lc-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-sys-0.41) >= 0.41.0
Provides:       crate(%{pkgname}/aws-lc-sys)
Provides:       crate(%{pkgname}/non-fips)

%description -n %{name}+aws-lc-sys
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "aws-lc-sys" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "non-fips" feature.

%package     -n %{name}+bindgen
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-fips-sys-0.13/bindgen) >= 0.13.1
Requires:       crate(aws-lc-sys-0.41/bindgen) >= 0.41.0
Provides:       crate(%{pkgname}/bindgen)

%description -n %{name}+bindgen
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "bindgen" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/aws-lc-sys)
Requires:       crate(%{pkgname}/ring-io)
Requires:       crate(%{pkgname}/ring-sig-verify)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "default" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "fips"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-fips-sys-0.13/default) >= 0.13.1
Provides:       crate(%{pkgname}/fips)

%description -n %{name}+fips
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "fips" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+legacy-des
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "legacy-des"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-sys-0.41/all-bindings) >= 0.41.0
Provides:       crate(%{pkgname}/legacy-des)

%description -n %{name}+legacy-des
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "legacy-des" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prebuilt-nasm
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "prebuilt-nasm"
Requires:       crate(%{pkgname})
Requires:       crate(aws-lc-sys-0.41/prebuilt-nasm) >= 0.41.0
Provides:       crate(%{pkgname}/prebuilt-nasm)

%description -n %{name}+prebuilt-nasm
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "prebuilt-nasm" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring-io
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "ring-io" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(untrusted-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}/ring-io)
Provides:       crate(%{pkgname}/ring-sig-verify)

%description -n %{name}+ring-io
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "ring-io" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ring-sig-verify" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
