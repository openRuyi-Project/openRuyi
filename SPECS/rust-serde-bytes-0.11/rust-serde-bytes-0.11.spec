# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_bytes
%global full_version 0.11.19
%global pkgname serde-bytes-0.11

Name:           rust-serde-bytes-0.11
Version:        0.11.19
Release:        %autorelease
Summary:        Rust crate "serde_bytes"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/bytes
#!RemoteAsset:  sha256:a5d440709e79d88e51ac01c4b72fc6cb7314017bb7da9eeff678aa94c10e3ea8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1) >= 1.0.220
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "serde_bytes"

%package     -n %{name}+alloc
Summary:        Optimized handling of `&[u8]` and `Vec<u8>` for Serde - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/alloc) >= 1.0.220
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust serde_bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Optimized handling of `&[u8]` and `Vec<u8>` for Serde - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/std) >= 1.0.220
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde_bytes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
