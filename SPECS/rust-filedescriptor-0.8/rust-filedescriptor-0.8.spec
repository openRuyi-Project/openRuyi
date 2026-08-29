# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name filedescriptor
%global full_version 0.8.3
%global pkgname filedescriptor-0.8

Name:           rust-filedescriptor-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "filedescriptor"
License:        MIT
URL:            https://github.com/wezterm/wezterm
#!RemoteAsset:  sha256:e40758ed24c9b2eeb76c35fb0aebc66c626084edd827e07e1552279814c6682d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/fileapi) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/namedpipeapi) >= 0.3.0
Requires:       crate(winapi-0.3/processenv) >= 0.3.0
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.0
Requires:       crate(winapi-0.3/winsock2) >= 0.3.0
Requires:       crate(winapi-0.3/winuser) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "filedescriptor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
