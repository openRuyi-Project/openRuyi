# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name time-core
%global full_version 0.1.9
%global pkgname time-core-0.1

Name:           rust-time-core-0.1
Version:        0.1.9
Release:        %autorelease
Summary:        Rust crate "time-core"
License:        MIT OR Apache-2.0
URL:            https://github.com/time-rs/time
#!RemoteAsset:  sha256:9e1c906769ad99c88eaa54e728060edef082f8e358ff32030cb7c7d315e81109
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/large-dates) = %{version}

%description
Source code for takopackized Rust crate "time-core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
