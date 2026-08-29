# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name r-efi
%global full_version 5.3.0
%global pkgname r-efi-5

Name:           rust-r-efi-5
Version:        5.3.0
Release:        %autorelease
Summary:        Rust crate "r-efi"
License:        MIT OR Apache-2.0 OR LGPL-2.1-or-later
URL:            https://github.com/r-efi/r-efi/wiki
#!RemoteAsset:  sha256:69cdb34c158ceb288df11e18b4bd39de994f6657d83847bdffdbd7f346754b0f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/efiapi) = %{version}
Provides:       crate(%{pkgname}/examples) = %{version}
Provides:       crate(%{pkgname}/native) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description
Source code for takopackized Rust crate "r-efi"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
