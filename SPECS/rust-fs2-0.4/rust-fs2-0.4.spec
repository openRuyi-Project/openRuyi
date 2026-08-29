# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fs2
%global full_version 0.4.3
%global pkgname fs2-0.4

Name:           rust-fs2-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "fs2"
License:        MIT OR Apache-2.0
URL:            https://github.com/danburkert/fs2-rs
#!RemoteAsset:  sha256:9564fc758e15025b46aa6643b1b77d047d1a56a1aea6e01002ac0c7026876213
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.30
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/fileapi) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.0
Requires:       crate(winapi-0.3/std) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fs2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
