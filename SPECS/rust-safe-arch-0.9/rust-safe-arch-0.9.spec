# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name safe_arch
%global full_version 0.9.3
%global pkgname safe-arch-0.9

Name:           rust-safe-arch-0.9
Version:        0.9.3
Release:        %autorelease
Summary:        Rust crate "safe_arch"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/safe_arch
#!RemoteAsset:  sha256:629516c85c29fe757770fa03f2074cf1eac43d44c02a3de9fc2ef7b0e207dfdd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "safe_arch"

%package     -n %{name}+bytemuck
Summary:        Crate that exposes `core::arch` safely via `#[cfg()]` - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust safe_arch crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
