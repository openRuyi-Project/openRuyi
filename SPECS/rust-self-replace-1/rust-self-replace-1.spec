# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name self-replace
%global full_version 1.5.0
%global pkgname self-replace-1

Name:           rust-self-replace-1
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "self-replace"
License:        Apache-2.0
URL:            https://github.com/mitsuhiko/self-replace
#!RemoteAsset:  sha256:03ec815b5eab420ab893f63393878d89c90fdd94c0bcc44c07abb8ad95552fb7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fastrand-2/default) >= 2.1.0
Requires:       crate(tempfile-3/default) >= 3.10.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-security) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-environment) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-libraryloader) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-memory) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-threading) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-shell) >= 0.52.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "self-replace"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
