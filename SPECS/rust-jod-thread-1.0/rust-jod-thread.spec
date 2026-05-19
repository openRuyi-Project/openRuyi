# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jod-thread
%global full_version 1.0.0
%global pkgname jod-thread-1.0

Name:           rust-jod-thread-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "jod-thread"
License:        MIT OR Apache-2.0
URL:            https://github.com/matklad/jod-thread
#!RemoteAsset:  sha256:a037eddb7d28de1d0fc42411f501b53b75838d313908078d6698d064f3029b24
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "jod-thread"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
