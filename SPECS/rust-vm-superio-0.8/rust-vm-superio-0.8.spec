# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vm-superio
%global full_version 0.8.1
%global pkgname vm-superio-0.8

Name:           rust-vm-superio-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "vm-superio"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/vm-superio
#!RemoteAsset:  sha256:69c376a9b84afdf97bddd2628096cf3554208b2a676cf06b4532e0f433a54e02
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vm-superio"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
