# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name is-terminal
%global full_version 0.4.17
%global pkgname is-terminal-0.4

Name:           rust-is-terminal-0.4
Version:        0.4.17
Release:        %autorelease
Summary:        Rust crate "is-terminal"
License:        MIT
URL:            https://github.com/sunfishcode/is-terminal
#!RemoteAsset:  sha256:3640c1c38b8e4e43584d8df18be5fc6b0aa314ce6ebf51b53313d4306cca8e46
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hermit-abi-0.5/default) >= 0.5.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-console) >= 0.52.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "is-terminal"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
