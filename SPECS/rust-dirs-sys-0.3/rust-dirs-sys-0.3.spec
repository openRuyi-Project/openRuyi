# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dirs-sys
%global full_version 0.3.7
%global pkgname dirs-sys-0.3

Name:           rust-dirs-sys-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "dirs-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/dirs-dev/dirs-sys-rs
#!RemoteAsset:  sha256:1b1d1d91c932ef41c0f2663aa8b0ca0342d444d842c06914aa0a7e352d0bada6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(redox-users-0.4) >= 0.4.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/knownfolders) >= 0.3.0
Requires:       crate(winapi-0.3/objbase) >= 0.3.0
Requires:       crate(winapi-0.3/shlobj) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dirs-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
