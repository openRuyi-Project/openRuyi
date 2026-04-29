# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tower-layer
%global full_version 0.3.3
%global pkgname tower-layer-0.3

Name:           rust-tower-layer-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "tower-layer"
License:        MIT
URL:            https://github.com/tower-rs/tower
#!RemoteAsset:  sha256:121c2a6cda46980bb0fcd1647ffaf6cd3fc79a013de288782836f6df9c48780e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tower-layer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
