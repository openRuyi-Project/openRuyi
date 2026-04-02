# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glob
%global full_version 0.3.3
%global pkgname glob-0.3

Name:           rust-glob-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "glob"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/glob
#!RemoteAsset:  sha256:0cc23270f6e1808e30a928bdc84dea0b9b4136a8bc82338574f23baf47bbd280
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "glob"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
