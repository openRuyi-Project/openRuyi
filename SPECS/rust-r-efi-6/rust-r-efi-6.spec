# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name r-efi
%global full_version 6.0.0
%global pkgname r-efi-6

Name:           rust-r-efi-6
Version:        6.0.0
Release:        %autorelease
Summary:        Rust crate "r-efi"
License:        MIT OR Apache-2.0 OR LGPL-2.1-or-later
URL:            https://github.com/r-efi/r-efi/wiki
#!RemoteAsset:  sha256:f8dcc9c7d52a811697d2151c701e0d08956f92b0e24136cf4cf27b57a6a0d9bf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/native) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description
Source code for takopackized Rust crate "r-efi"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
