# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pxfm
%global full_version 0.1.29
%global pkgname pxfm-0.1

Name:           rust-pxfm-0.1
Version:        0.1.29
Release:        %autorelease
Summary:        Rust crate "pxfm"
License:        BSD-3-Clause OR Apache-2.0
URL:            https://github.com/awxkee/pxfm
#!RemoteAsset:  sha256:e0c5ccf5294c6ccd63a74f1565028353830a9c2f5eb0c682c355c471726a6e3f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pxfm"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
