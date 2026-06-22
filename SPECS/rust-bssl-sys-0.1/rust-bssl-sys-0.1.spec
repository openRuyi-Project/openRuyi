# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bssl-sys
%global full_version 0.1.0
%global pkgname bssl-sys-0.1

Name:           rust-bssl-sys-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "bssl-sys"
License:        MIT
URL:            FIXME
#!RemoteAsset:  sha256:312d12393c060384f2e6ed14c7b4be37b3dd90249857485613c1a91b9a1abb5c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bssl-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
