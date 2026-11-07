# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name utf8-ranges
%global full_version 0.1.3
%global pkgname utf8-ranges-0.1

Name:           rust-utf8-ranges-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "utf8-ranges"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/utf8-ranges
#!RemoteAsset:  sha256:a1ca13c08c41c9c3e04224ed9ff80461d97e121589ff27c753a16cb10830ae0f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "utf8-ranges"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
