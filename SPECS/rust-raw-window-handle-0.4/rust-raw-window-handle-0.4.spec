# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name raw-window-handle
%global full_version 0.4.3
%global pkgname raw-window-handle-0.4

Name:           rust-raw-window-handle-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "raw-window-handle"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/rust-windowing/raw-window-handle
#!RemoteAsset:  sha256:b800beb9b6e7d2df1fe337c9e3d04e3af22a124460fb4c30fcc22c9117cefb41
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cty-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "raw-window-handle"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
