# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ripemd
%global full_version 0.1.3
%global pkgname ripemd-0.1

Name:           rust-ripemd-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "ripemd"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:bd124222d17ad93a644ed9d011a40f4fb64aa54275c08cc216524a9ea82fb09f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.10/default) >= 0.10.4

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ripemd"

%package     -n %{name}+oid
Summary:        Pure Rust implementation of the RIPEMD hash functions - feature "oid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/oid) >= 0.10.4
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust ripemd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the RIPEMD hash functions - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/std) >= 0.10.4
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ripemd crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
