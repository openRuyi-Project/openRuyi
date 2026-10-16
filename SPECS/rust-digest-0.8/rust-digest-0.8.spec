# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name digest
%global full_version 0.8.1
%global pkgname digest-0.8

Name:           rust-digest-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "digest"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:f3d0c8c8752312f9713efd397ff63acb9f85585afbf179282e720e7704954dd5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(generic-array-0.12/default) >= 0.12.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "digest"

%package     -n %{name}+blobby
Summary:        Traits for cryptographic hash functions - feature "blobby" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(blobby-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/blobby) = %{version}
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
