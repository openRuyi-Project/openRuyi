# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linux-loader
%global full_version 0.14.0
%global pkgname linux-loader-0.14

Name:           rust-linux-loader-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "linux-loader"
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/rust-vmm/linux-loader
#!RemoteAsset:  sha256:d54207cb617cd75b10c57ad20235c914ab62b180ceeff2ef3111983670d3b321
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(vm-memory-0.18/default) >= 0.18.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bzimage) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/elf) = %{version}
Provides:       crate(%{pkgname}/pe) = %{version}

%description
Source code for the Rust crate "linux-loader"

%files
%license LICENSE-APACHE LICENSE-BSD-3-Clause
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
