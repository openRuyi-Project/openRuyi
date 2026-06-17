# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wide
%global full_version 0.7.33
%global pkgname wide-0.7

Name:           rust-wide-0.7
Version:        0.7.33
Release:        %autorelease
Summary:        Rust crate "wide"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/wide
#!RemoteAsset:  sha256:0ce5da8ecb62bcd8ec8b7ea19f69a51275e91299be594ea5cc6ef7819e16cd03
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytemuck-1/default) >= 1.0.0
Requires:       crate(safe-arch-0.7/bytemuck) >= 0.7.0
Requires:       crate(safe-arch-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "wide"

%package     -n %{name}+serde
Summary:        Help you go wide - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wide crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
