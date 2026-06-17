# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name debug-helper
%global full_version 0.3.13
%global pkgname debug-helper-0.3

Name:           rust-debug-helper-0.3
Version:        0.3.13
Release:        %autorelease
Summary:        Rust crate "debug-helper"
License:        MIT
URL:            https://magiclen.org/debug-helper
#!RemoteAsset:  sha256:f578e8e2c440e7297e008bb5486a3a8a194775224bbc23729b0dbdfaeebf162e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "debug-helper"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
