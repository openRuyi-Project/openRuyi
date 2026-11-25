# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytestring
%global full_version 1.5.1
%global pkgname bytestring-1

Name:           rust-bytestring-1
Version:        1.5.1
Release:        %autorelease
Summary:        Rust crate "bytestring"
License:        MIT OR Apache-2.0
URL:            https://actix.rs
#!RemoteAsset:  sha256:86566c496f2f47d9b8147a4c8b02ffdb69c919fe0c2b2e7195d22cbba0e635c9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1) >= 1.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bytestring"

%package     -n %{name}+serde
Summary:        UTF-8 encoded read-only string using `Bytes` as storage - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bytestring crate, by
pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
