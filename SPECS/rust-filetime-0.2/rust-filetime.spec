# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name filetime
%global full_version 0.2.24
%global pkgname filetime-0.2

Name:           rust-filetime-0.2
Version:        0.2.24
Release:        %autorelease
Summary:        Rust crate "filetime"
License:        MIT/Apache-2.0
URL:            https://github.com/alexcrichton/filetime
#!RemoteAsset:  sha256:bf401df4a4e3872c4fe8151134cf483738e74b67fc934d6532c882b3d24a4550
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.169
Requires:       crate(libredox-0.1/default) >= 0.1.3
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-storage-filesystem) >= 0.59.0
Provides:       crate(filetime) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "filetime"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
