# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ptyprocess
%global full_version 0.5.0
%global pkgname ptyprocess-0.5

Name:           rust-ptyprocess-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "ptyprocess"
License:        MIT
URL:            https://github.com/zhiburt/ptyprocess
#!RemoteAsset:  sha256:101be273c0b1680d7056afddbaa88f02b6e9f2dc161165c30bee9914b6025a79
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nix-0.26/default) >= 0.26.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/close-range) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ptyprocess"

%files
%license LICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
