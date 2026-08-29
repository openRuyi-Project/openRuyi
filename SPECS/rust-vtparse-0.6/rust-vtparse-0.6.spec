# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vtparse
%global full_version 0.6.2
%global pkgname vtparse-0.6

Name:           rust-vtparse-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "vtparse"
License:        MIT
URL:            https://github.com/wez/wezterm
#!RemoteAsset:  sha256:6d9b2acfb050df409c972a37d3b8e08cdea3bddb0c09db9d53137e504cfabed0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(utf8parse-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vtparse"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
