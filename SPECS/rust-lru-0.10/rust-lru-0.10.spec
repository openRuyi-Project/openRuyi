# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global crate_name lru
%global full_version 0.10.1
%global pkgname lru-0.10

Name:           rust-lru-0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Rust crate "lru"
License:        MIT
URL:            https://github.com/jeromefroe/lru-rs
#!RemoteAsset:  sha256:718e8fae447df0c7e1ba7f5189829e63fd536945c8988d61444c19039f16b670
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lru"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
