# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name maybe-uninit
%global full_version 2.0.0
%global pkgname maybe-uninit-2

Name:           rust-maybe-uninit-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "maybe-uninit"
License:        Apache-2.0 OR MIT
URL:            https://github.com/est31/maybe-uninit
#!RemoteAsset:  sha256:60302e4db3a61da70c0cb7991976248362f30319e88850c487b9b95bbf059e00
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "maybe-uninit"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
