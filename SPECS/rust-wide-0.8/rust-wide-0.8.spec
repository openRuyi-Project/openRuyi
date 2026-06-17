# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wide
%global full_version 0.8.3
%global pkgname wide-0.8

Name:           rust-wide-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "wide"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/wide
#!RemoteAsset:  sha256:13ca908d26e4786149c48efcf6c0ea09ab0e06d1fe3c17dc1b4b0f1ca4a7e788
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytemuck-1/default) >= 1.24.0
Requires:       crate(safe-arch-0.9/bytemuck) >= 0.9.2
Requires:       crate(safe-arch-0.9/default) >= 0.9.2
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
