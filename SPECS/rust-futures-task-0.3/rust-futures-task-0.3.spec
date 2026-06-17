# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-task
%global full_version 0.3.32
%global pkgname futures-task-0.3

Name:           rust-futures-task-0.3
Version:        0.3.32
Release:        %autorelease
Summary:        Rust crate "futures-task"
License:        MIT OR Apache-2.0
URL:            https://rust-lang.github.io/futures-rs
#!RemoteAsset:  sha256:037711b3d59c33004d3856fbdc83b99d4ff37a24768fa1be9ce3538a1cde4393
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/cfg-target-has-atomic) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "futures-task"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
