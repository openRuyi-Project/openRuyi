# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wezterm-dynamic-derive
%global full_version 0.1.1
%global pkgname wezterm-dynamic-derive-0.1

Name:           rust-wezterm-dynamic-derive-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "wezterm-dynamic-derive"
License:        MIT
URL:            https://github.com/wezterm/wezterm
#!RemoteAsset:  sha256:46c0cf2d539c645b448eaffec9ec494b8b19bd5077d9e58cb1ae7efece8d575b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.2
Requires:       crate(syn-1/default) >= 1.0.0
Requires:       crate(syn-1/extra-traits) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wezterm-dynamic-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
