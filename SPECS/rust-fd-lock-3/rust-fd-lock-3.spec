# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fd-lock
%global full_version 3.0.13
%global pkgname fd-lock-3

Name:           rust-fd-lock-3
Version:        3.0.13
Release:        %autorelease
Summary:        Rust crate "fd-lock"
License:        MIT OR Apache-2.0
URL:            https://github.com/yoshuawuyts/fd-lock
#!RemoteAsset:  sha256:ef033ed5e9bad94e55838ca0ca906db0e043f517adda0c8b79c7a8c66c93c1b5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(rustix-0.38/default) >= 0.38.0
Requires:       crate(rustix-0.38/fs) >= 0.38.0
Requires:       crate(windows-sys-0.48/default) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-foundation) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-storage-filesystem) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-io) >= 0.48.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fd-lock"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
