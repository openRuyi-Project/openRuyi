# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name avt
%global full_version 0.18.0
%global pkgname avt-0.18

Name:           rust-avt-0.18
Version:        0.18.0
Release:        %autorelease
Summary:        Rust crate "avt"
License:        Apache-2.0
URL:            https://github.com/asciinema/avt
#!RemoteAsset:  sha256:7179c44abe2ac36173d4713bfed24136e5988f005c7fe2c4fcde621d3d4d29b9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rgb-0.8/default) >= 0.8.33
Requires:       crate(unicode-width-0.1/default) >= 0.1.13

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "avt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
