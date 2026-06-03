# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fs_extra
%global full_version 1.3.0
%global pkgname fs-extra-1.0

Name:           rust-fs-extra-1.0
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "fs_extra"
License:        MIT
URL:            https://github.com/webdesus/fs_extra
#!RemoteAsset:  sha256:42703706b716c37f96a77aea830392ad231f44c9e9a67872fa5548707e11b11c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Recursively copy folders with information about process and much more.
Source code for takopackized Rust crate "fs_extra"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
