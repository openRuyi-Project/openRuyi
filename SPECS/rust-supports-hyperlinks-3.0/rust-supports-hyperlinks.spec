# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name supports-hyperlinks
%global full_version 3.2.0
%global pkgname supports-hyperlinks-3.0

Name:           rust-supports-hyperlinks-3.0
Version:        3.2.0
Release:        %autorelease
Summary:        Rust crate "supports-hyperlinks"
License:        Apache-2.0
URL:            https://github.com/zkat/supports-hyperlinks
#!RemoteAsset:  sha256:e396b6523b11ccb83120b115a0b7366de372751aa6edf19844dfb13a6af97e91
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "supports-hyperlinks"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
