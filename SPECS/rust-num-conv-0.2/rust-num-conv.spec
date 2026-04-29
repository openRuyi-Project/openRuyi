# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-conv
%global full_version 0.2.1
%global pkgname num-conv-0.2

Name:           rust-num-conv-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "num-conv"
License:        MIT OR Apache-2.0
URL:            https://github.com/jhpratt/num-conv
#!RemoteAsset:  sha256:c6673768db2d862beb9b39a78fdcb1a69439615d5794a1be50caa9bc92c81967
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
This provides better certainty when refactoring, makes the exact behavior of code more explicit, and allows using turbofish syntax.
Source code for takopackized Rust crate "num-conv"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
