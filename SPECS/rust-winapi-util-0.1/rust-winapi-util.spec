# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winapi-util
%global full_version 0.1.9
%global pkgname winapi-util-0.1

Name:           rust-winapi-util-0.1
Version:        0.1.9
Release:        %autorelease
Summary:        Rust crate "winapi-util"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/winapi-util
#!RemoteAsset:  sha256:cf221c93e13a30d793f7645a0e7762c55d169dbb0a49671918a2319d289b10bb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-storage-filesystem) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-console) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-systeminformation) >= 0.59.0
Provides:       crate(winapi-util) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "winapi-util"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
