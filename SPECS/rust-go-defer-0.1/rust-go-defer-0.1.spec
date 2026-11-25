# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name go-defer
%global full_version 0.1.0
%global pkgname go-defer-0.1

Name:           rust-go-defer-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "go-defer"
License:        Apache-2.0
URL:            FIXME
#!RemoteAsset:  sha256:4053f727e8be72cb6afd9f05955676f4df66b2f6a56c5b29362403df8810062b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "go-defer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
