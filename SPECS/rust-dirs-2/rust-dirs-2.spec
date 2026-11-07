# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dirs
%global full_version 2.0.2
%global pkgname dirs-2

Name:           rust-dirs-2
Version:        2.0.2
Release:        %autorelease
Summary:        Rust crate "dirs"
License:        MIT OR Apache-2.0
URL:            https://github.com/soc/dirs-rs
#!RemoteAsset:  sha256:13aea89a5c93364a98e9b37b2fa237effbb694d5cfe01c5b70941f7eb087d5e3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-0.1/default) >= 0.1.0
Requires:       crate(dirs-sys-0.3/default) >= 0.3.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dirs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
