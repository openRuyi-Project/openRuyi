# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name is_executable
%global full_version 1.0.5
%global pkgname is-executable-1.0

Name:           rust-is-executable-1.0
Version:        1.0.5
Release:        %autorelease
Summary:        Rust crate "is_executable"
License:        MIT OR Apache-2.0
URL:            https://github.com/fitzgen/is_executable
#!RemoteAsset:  sha256:baabb8b4867b26294d818bf3f651a454b6901431711abb96e296245888d6e8c4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-sys-0.60/default) >= 0.60.2
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "is_executable"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
