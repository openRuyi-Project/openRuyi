# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anstyle-svg
%global full_version 0.1.12
%global pkgname anstyle-svg-0.1

Name:           rust-anstyle-svg-0.1
Version:        0.1.12
Release:        %autorelease
Summary:        Rust crate "anstyle-svg"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/anstyle.git
#!RemoteAsset:  sha256:e22d9f3dea8bbda97c75bd0f0203e23f1e190d6d6f27a40e10063946dc4d4362
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(anstyle-lossy-1.0/default) >= 1.1.5
Requires:       crate(anstyle-parse-0.2/default) >= 0.2.7
Requires:       crate(html-escape-0.2/default) >= 0.2.13
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "anstyle-svg"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
