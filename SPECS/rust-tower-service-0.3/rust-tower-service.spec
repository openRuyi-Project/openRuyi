# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tower-service
%global full_version 0.3.3
%global pkgname tower-service-0.3

Name:           rust-tower-service-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "tower-service"
License:        MIT
URL:            https://github.com/tower-rs/tower
#!RemoteAsset:  sha256:8df9b6e13f2d32c91b9bd719c00d1958837bc7dec474d94952798cc8e69eeec3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tower-service"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
