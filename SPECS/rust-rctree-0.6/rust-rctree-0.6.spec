# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rctree
%global full_version 0.6.0
%global pkgname rctree-0.6

Name:           rust-rctree-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "rctree"
License:        MIT
URL:            https://github.com/RazrFalcon/rctree
#!RemoteAsset:  sha256:e03e7866abec1101869ffa8e2c8355c4c2419d0214ece0cc3e428e5b94dea6e9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rctree"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
