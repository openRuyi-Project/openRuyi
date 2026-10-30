# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name device_tree
%global full_version 1.1.0
%global pkgname device-tree-1

Name:           rust-device-tree-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "device_tree"
License:        MIT
URL:            https://github.com/mbr/device_tree-rs
#!RemoteAsset:  sha256:f18f717c5c7c2e3483feb64cccebd077245ad6d19007c2db0fd341d38595353c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Reads and parses Linux device tree images.
Source code for takopackized Rust crate "device_tree"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
