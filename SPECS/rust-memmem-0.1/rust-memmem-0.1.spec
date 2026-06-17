# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memmem
%global full_version 0.1.1
%global pkgname memmem-0.1

Name:           rust-memmem-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "memmem"
License:        MIT OR Apache-2.0
URL:            http://github.com/jneem/memmem
#!RemoteAsset:  sha256:a64a92489e2744ce060c349162be1c5f33c6969234104dbd99ddb5feb08b8c15
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "memmem"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
