# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name daemonix
%global full_version 0.1.0
%global pkgname daemonix-0.1

Name:           rust-daemonix-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "daemonix"
License:        MIT OR Apache-2.0
URL:            https://codeberg.org/commons-rs/daemonix
#!RemoteAsset:  sha256:f0b747381562a10fd2104e9333ad72fe5158d79de81b64426fc9e229c6d3fb38
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.98

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "daemonix"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
