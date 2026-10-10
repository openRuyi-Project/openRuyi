# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vcell
%global full_version 0.1.3
%global pkgname vcell-0.1

Name:           rust-vcell-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "vcell"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/vcell
#!RemoteAsset:  sha256:77439c1b53d2303b20d9459b1ade71a83c716e3f9c34f3228c00e6f185d6c002
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/const-fn) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vcell"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
