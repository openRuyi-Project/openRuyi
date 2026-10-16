# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name streaming-stats
%global full_version 0.1.29
%global pkgname streaming-stats-0.1

Name:           rust-streaming-stats-0.1
Version:        0.1.29
Release:        %autorelease
Summary:        Rust crate "streaming-stats"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/rust-stats
#!RemoteAsset:  sha256:dbc32bf233385fb1ae0c4cf13a8dfd11efec71f6a9de95feac8c870788bc8b25
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "streaming-stats"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
