# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aws-lc-rs
%global full_version 1.15.2
%global pkgname aws-lc-rs-1

Name:           rust-aws-lc-rs-1
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

Requires:       crate(zeroize-1/default) >= 1.8.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/test-logging) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
This library strives to be API-compatible with the popular Rust library named ring.
Source code for takopackized Rust crate "aws-lc-rs"

%package     -n %{name}+asan
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "asan"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-fips-sys-0.13/asan) >= 0.13.1
Requires:       crate(aws-lc-sys-0.35/asan) >= 0.35.0
Provides:       crate(%{pkgname}/asan) = %{version}

%description -n %{name}+asan
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "asan" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-sys
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "aws-lc-sys" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-sys-0.35) >= 0.35.0
Provides:       crate(%{pkgname}/aws-lc-sys) = %{version}
Provides:       crate(%{pkgname}/non-fips) = %{version}

%description -n %{name}+aws-lc-sys
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "aws-lc-sys" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "non-fips" feature.

%package     -n %{name}+bindgen
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-fips-sys-0.13/bindgen) >= 0.13.1
Requires:       crate(aws-lc-sys-0.35/bindgen) >= 0.35.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "bindgen" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/aws-lc-sys) = %{version}
Requires:       crate(%{pkgname}/ring-io) = %{version}
Requires:       crate(%{pkgname}/ring-sig-verify) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "default" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-fips-sys-0.13/default) >= 0.13.1
Provides:       crate(%{pkgname}/fips) = %{version}

%description -n %{name}+fips
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "fips" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prebuilt-nasm
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "prebuilt-nasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-sys-0.35/prebuilt-nasm) >= 0.35.0
Provides:       crate(%{pkgname}/prebuilt-nasm) = %{version}

%description -n %{name}+prebuilt-nasm
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "prebuilt-nasm" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring-io
Summary:        Cryptographic library using AWS-LC for its cryptographic operations - feature "ring-io" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(untrusted-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}/ring-io) = %{version}
Provides:       crate(%{pkgname}/ring-sig-verify) = %{version}

%description -n %{name}+ring-io
This library strives to be API-compatible with the popular Rust library named ring.
This metapackage enables feature "ring-io" for the Rust aws-lc-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ring-sig-verify" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
