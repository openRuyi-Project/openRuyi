# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cfg_aliases
%global full_version 0.2.1
%global pkgname cfg-aliases-0.2

Name:           rust-cfg-aliases-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "cfg_aliases"
License:        MIT
URL:            https://github.com/katharostech/cfg_aliases
#!RemoteAsset:  sha256:613afe47fcd5fac7ccf1db93babcb082c5994d996f20b8b159f2ad1658eb5724
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cfg_aliases"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
