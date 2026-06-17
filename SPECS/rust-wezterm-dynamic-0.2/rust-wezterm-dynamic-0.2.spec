# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wezterm-dynamic
%global full_version 0.2.1
%global pkgname wezterm-dynamic-0.2

Name:           rust-wezterm-dynamic-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "wezterm-dynamic"
License:        MIT
URL:            https://github.com/wezterm/wezterm
#!RemoteAsset:  sha256:5f2ab60e120fd6eaa68d9567f3226e876684639d22a4219b313ff69ec0ccd5ac
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(ordered-float-4/default) >= 4.1.0
Requires:       crate(strsim-0.11/default) >= 0.11.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(wezterm-dynamic-derive-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wezterm-dynamic"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
