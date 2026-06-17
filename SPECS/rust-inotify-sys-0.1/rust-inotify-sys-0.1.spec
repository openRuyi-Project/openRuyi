# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name inotify-sys
%global full_version 0.1.5
%global pkgname inotify-sys-0.1

Name:           rust-inotify-sys-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "inotify-sys"
License:        ISC
URL:            https://github.com/hannobraun/inotify-sys
#!RemoteAsset:  sha256:e05c02b5e89bff3b946cedeca278abc628fe811e604f027c45a8aa3cf793d0eb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "inotify-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
