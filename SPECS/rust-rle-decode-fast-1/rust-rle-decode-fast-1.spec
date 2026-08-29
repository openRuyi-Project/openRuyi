# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rle-decode-fast
%global full_version 1.0.3
%global pkgname rle-decode-fast-1

Name:           rust-rle-decode-fast-1
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "rle-decode-fast"
License:        MIT OR Apache-2.0
URL:            https://github.com/WanzenBug/rle-decode-helper
#!RemoteAsset:  sha256:3582f63211428f83597b51b2ddb88e2a91a9d52d12831f9d08f5e624e8977422
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Previsouly, the fastest way to implement any kind of decoding for Run Length Encoded data in Rust.
Source code for takopackized Rust crate "rle-decode-fast"

%package     -n %{name}+criterion
Summary:        Deprecated: this is available in stable Rust since 1.53 as Vec::extend_from_within() - feature "criterion" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(criterion-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/bench) = %{version}
Provides:       crate(%{pkgname}/criterion) = %{version}

%description -n %{name}+criterion
Previsouly, the fastest way to implement any kind of decoding for Run Length Encoded data in Rust.
This metapackage enables feature "criterion" for the Rust rle-decode-fast crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bench" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
