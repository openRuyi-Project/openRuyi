# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name plotters-backend
%global full_version 0.3.7
%global pkgname plotters-backend-0.3

Name:           rust-plotters-backend-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "plotters-backend"
License:        MIT
URL:            https://plotters-rs.github.io
#!RemoteAsset:  sha256:df42e13c12958a16b3f7f4386b9ab1f3e7933914ecea48da7139435263a4172a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "plotters-backend"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
