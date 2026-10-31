# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memfd
%global full_version 0.6.5
%global pkgname memfd-0.6

Name:           rust-memfd-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "memfd"
License:        MIT OR Apache-2.0
URL:            https://github.com/lucab/memfd-rs
#!RemoteAsset:  sha256:ad38eb12aea514a0466ea40a80fd8cc83637065948eb4a426e4aa46261175227
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustix-1/default) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "memfd"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
