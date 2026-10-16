# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tagptr
%global full_version 0.2.0
%global pkgname tagptr-0.2

Name:           rust-tagptr-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "tagptr"
License:        MIT OR Apache-2.0
URL:            https://github.com/oliver-giersch/tagptr.git
#!RemoteAsset:  sha256:7b2093cf4c8eb1e67749a6762251bc9cd836b6fc171623bd0a9d324d37af2417
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tagptr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
