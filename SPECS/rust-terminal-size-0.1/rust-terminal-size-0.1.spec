# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name terminal_size
%global full_version 0.1.17
%global pkgname terminal-size-0.1

Name:           rust-terminal-size-0.1
Version:        0.1.17
Release:        %autorelease
Summary:        Rust crate "terminal_size"
License:        MIT OR Apache-2.0
URL:            https://github.com/eminence/terminal-size
#!RemoteAsset:  sha256:633c1a546cee861a1a6d0dc69ebeca693bf4296661ba7852b9d21d159e0506df
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/processenv) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0
Requires:       crate(winapi-0.3/wincon) >= 0.3.0
Requires:       crate(winapi-0.3/winnt) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "terminal_size"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
