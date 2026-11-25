# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name transform-stream
%global full_version 0.3.1
%global pkgname transform-stream-0.3

Name:           rust-transform-stream-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "transform-stream"
License:        MIT
URL:            https://github.com/Nugine/transform-stream
#!RemoteAsset:  sha256:c1a814d25437963577f6221d33a2aaa60bfb44acc3330cdc7c334644e9832022
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3/default) >= 0.3.31

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "transform-stream"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
